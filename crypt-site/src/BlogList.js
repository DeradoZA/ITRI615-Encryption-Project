function BlogList({blogs, title}){

    return(
        <div>
            <h1>{title}</h1>
            <div className="blog-list">
                {blogs.map((blog) => (
                    <div className="blog-preview" key={blog.id}>
                        <h2>{blog.title}</h2>
                        <p>{blog.author}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default BlogList