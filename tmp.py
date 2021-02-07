from models import Post, Tag
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
    """
    Saving article to database
    :param my_post - object of article, type - Post:
    :return:
    """
    db.session.add(my_post)
    db.session.commit()


@check_for_type(Tag)
def save_tag_to_db(tag):
    """
    Saving tags to database. Further - do polimorfism with save_post_to_db by decorator
    :param tag - object of tag, type - Tag:
    :return:
    """
    #print()
    #print(f'its begining of save_tag_to_db. Parametr, tag, is {tag}')
    db.session.add(tag)
    db.session.commit()


def get_articles():
    """
    This function returns dict of some articles.
    :key - name of article
    :value - body of article
    :return dict of articles :
    """
    my_dict = {
        'Pinn and hunger assembly' : ZEROES_ARTICLE,
        'Special Delivery' : FIRST_ARTICLE,
        'Great Five-year Video of the Sun' : SECOND_ARTICLE,
        'Man Destroys COVID-19 Vaccine ' : THIRD_ARTICLE,
        'Hedgehog Café in Tokyo' : FOURTH_ARTICLE,
        'Christmas in Europe' : FIFTH_ARTICLE,
        'Christmas Lights' : SIXTH_ARTICLE,
        'Moon Landing' : SEVENTH_ARTICLE
    }
    return my_dict


def do_post(title, body):
    """
    Creating object of Post
    :param title:  name of article
    :param body:  body of article
    :return:  object of Post
    """
    return Post(title = title,
                body = body)


def create_articles():
    """
    Creating and saving to database posts
    :return: Nothing
    """
    my_articles = get_articles()
    for i in my_articles:
        my_post = do_post(i, my_articles[i])
        save_post_to_db(my_post)


def get_posts():
    """
    Takes from database all Posts
    :return: - list_of_posts
    """
    #print('its begining of function get_posts')
    list_of_posts = Post.query.all()
    #print(f'its end of function get_posts. List_of_posts = {list_of_posts}')
    return list_of_posts


def get_tags_by_slug(slug):
    """

    :param slug: slug of posts
    :return: list of tags
    """
    #print()
    #print(f'its begining of function get_tags_by_slag. Parametr, slug, is {slug}')
    my_list = slug.split('-')
    set_of_bad_words = {'not', 'and', 'or', 'of', 'in'}
    my_list = list(set(my_list)- set_of_bad_words)
    my_list = [i for i in my_list if not i.isdecimal()]
    #print(f'its ending of function get_tags_by_slag. my_list is {my_list}')
    return my_list


def get_tags(list_of_posts):
    #print()
    #print('its begining of function list_of_posts')
    my_tags = []
    for i in list_of_posts:
        tmp_tag = get_tags_by_slug(i.slug)
        my_tags += tmp_tag
    #print(f'its ending of function get_tags. My_Tags = {my_tags}')
    #print()
    return my_tags


def register_tag(tag):
    """
    Saving one tag to database
    :param tag: object Tag
    :return:
    """
    #print()
    #print(f'its begining of function register_tag. Parametr, tag, is {tag}')
    my_tag = Tag(name = tag)
    #print('-----------------------------------------------------------')
    #print(f'here we have my_tag = {my_tag}')
    try:
        save_tag_to_db(my_tag)
    except Exception:
        pass
    #print('its ending of function register_tag')


def register_all_tags(list_of_tags):
    """
    Saving list_of_tags to database
    :param list_of_tags:  list of tags (str)
    :return: Nothing
    """
    #print()
    #print(f'its begining of function register_all_tags. Parametr, list_of_tags is {list_of_tags}')
    for i in list_of_tags:
        register_tag(i)
    #print(f'its ending of register_all_tags')


def main():
    #create_articles()
    #print('its comment before getting list_of_posts')
    list_of_posts = get_posts()
    #print(f'its comment after getting list of posts. List of posts = {list_of_posts}')
    #print()

    #print('its comment before getting tags')
    my_tags = get_tags(list_of_posts)
    #print(f'its comment after getting tags. My_tags = {my_tags}')
    #print()

    #print('its comment after register_all_tags')
    register_all_tags(my_tags)
    #print('its comment after register_all_tags')


if __name__ == '__main__':
    main()
#db.create_all()
#my_title = 'pinn and hunger assembly'
#my_body = 'Once upon a time I walk near my house and shoot birds using my minigan. That was very funny because i have 1 billion dollars because of my own project AllMemes'
#my_post = Post(title = my_title, body = my_body)
#db.session.add(my_post)
#db.session.commit()