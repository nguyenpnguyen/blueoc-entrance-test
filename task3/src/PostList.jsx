import { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { fetchPosts } from './redux/postsSlice'
import Post from './Post'

const PostList = () => {

  const dispatch = useDispatch()
  const { items, status, error } = useSelector(state => state.posts)

  useEffect(() => {
    if (status === 'idle') {
      const fetchData = async () => {
        try {
          const result = await dispatch(fetchPosts()).unwrap()
          console.log('Fetched posts:', result)
        } catch (err) {
          console.error('Fetch error:', err)
        }
      }

      fetchData()
    }
  }, [status, dispatch])

  if (status === 'loading') return <p>Loading…</p>
  if (status === 'failed') return <p>Error: {error}</p>

  return (
    <>
      <ul>
        {items.map(post => (
          <Post key={post.id} post={post} />
        ))}
      </ul>
    </>
  )
}

export default PostList
