const Post = ({ post }) => {
  return (
    <li key={post.id}>
      <h2>User: {post.userId}</h2>
      <h3>{post.title}</h3>
      <p>{post.body}</p>
      <br />
    </li>
  )
}

export default Post
