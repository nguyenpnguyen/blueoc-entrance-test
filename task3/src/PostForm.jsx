import { useState } from 'react'
import { useDispatch } from 'react-redux'
import { createPost } from './redux/postsSlice'

const PostForm = () => {
  const dispatch = useDispatch()

  const [title, setTitle] = useState('')
  const [body, setBody] = useState('')
  const [userId, setUserId] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (title && body && userId) {
      try {
        await dispatch(createPost({ title, body, userId: Number(userId) })).unwrap()
        setTitle('')
        setBody('')
        setUserId('')
      } catch (err) {
        console.error('Failed to save the post:', err)
      }
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h3>Add New Post</h3>
      <input
        type="text"
        placeholder="User ID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
      />
      <br />
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <br />
      <textarea
        placeholder="Body"
        value={body}
        onChange={(e) => setBody(e.target.value)}
      />
      <br />
      <button type="submit">Add Post</button>
    </form>
  )
}

export default PostForm
