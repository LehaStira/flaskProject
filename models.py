from app import db
from datetime import datetime
import re
from reformat_strings import delete_reapiting
from reformat_strings import delete_last_symbol


def slugify(s):
    my_pattern = r'[^\w+]'
    print(f'My title is {s}')
    my_res = re.sub(my_pattern, '-', s)
    print(f'my_res after re is {my_res}')
    my_res = delete_last_symbol(my_res)
    my_res = delete_reapiting(my_res)
    return my_res.lower()


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(140), nullable = False)
    slug = db.Column(db.String(140),
                     nullable = False,
                     unique=True)
    body = db.Column(db.TEXT(), nullable = False)
    created = db.Column(db.DateTime(), default = datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f'<Post id is {self.id}, title is {self.title}>'