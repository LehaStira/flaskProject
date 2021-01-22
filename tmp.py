from models import Post
from app import db



my_title = 'pinn and hunger assembly'
my_body = 'Once upon a time I walk near my house and shoot birds using my minigan. That was very funny because i have 1 billion dollars because of my own project AllMemes'
my_post = Post(title = my_title, body = my_body)
db.session.add(my_post)
db.session.commit()