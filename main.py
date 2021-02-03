from app import app
import view
from app import db
import models
from posts.blueprint import posts


app.register_blueprint(posts, url_prefix = '/blog')


if __name__ == '__main__':
    app.run()