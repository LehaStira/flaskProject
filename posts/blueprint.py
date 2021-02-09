from flask import Blueprint
from flask import render_template
from models import Post, Tag
posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    my_posts = Post.query.all()
    return render_template('posts/index.html', my_posts = my_posts)


@posts.route('/<slug>')
def post_detail(slug):
    my_post = Post.query.filter(Post.slug == slug).first()
    my_tags = my_post.tags
    return render_template('posts/post_detail.html', post = my_post, tags = my_tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag_query = Tag.query.filter(Tag.slug==slug)
    tag = tag_query.first()
    posts = tag.posts.all()
    return render_template('/posts/tag_detail.html', posts = posts, tag = tag )