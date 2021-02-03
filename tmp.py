from models import Post
from app import db
from test import *


def check_for_type(type):
    def decorator(func):
        def wrapped(a):
            if not isinstance(a, type):
                raise ValueError(f"Bad data. Data type for argument {a} must be {type}")
            res = func(a)
            return res
        return wrapped
    return decorator


@check_for_type(Post)
def save_post_to_db(my_post):
    db.session.add(my_post)
    db.session.commit()


def get_articles():
    my_dict = {
        'Special Delivery' : FIRST_ARTICLE,
        'Great Five-year Video of the Sun' : SECOND_ARTICLE,
        'Man Destroys COVID-19 Vaccine ' : THIRD_ARTICLE,
        'Hedgehog Café in Tokyo' : FOURTH_ARTICLE,
        'Christmas in Europe' : FIFTH_ARTICLE,
        'Christmas Lights' : SIXTH_ARTICLE,
        'Moon Landing' : SEVENTH_ARTICLE
    }
    return my_dict


def get_post(title, body):
    return Post(title = title,
                body = body)


def main():
    my_articles = get_articles()
    for i in my_articles:
        my_post = get_post(i, my_articles[i])
        save_post_to_db(my_post)




if __name__ == '__main__':
    main()
#db.create_all()
#my_title = 'pinn and hunger assembly'
#my_body = 'Once upon a time I walk near my house and shoot birds using my minigan. That was very funny because i have 1 billion dollars because of my own project AllMemes'
#my_post = Post(title = my_title, body = my_body)
#db.session.add(my_post)
#db.session.commit()