from flask import Blueprint
from flask import render_template
from models import Post
posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    my_posts = Post.query.all()
    return render_template('posts/index.html', my_posts = my_posts)


@posts.route('/<slug>')
def post_detail(slug):
    my_post = Post.query.filter(Post.slug == slug).first()
    return render_template('posts/post_detail.html', post = my_post)