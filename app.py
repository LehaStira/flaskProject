from flask import Flask
from conf import Configuration
from posts.blueprint import posts
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(posts, url_prefix = '/blog')
db = SQLAlchemy(app)
