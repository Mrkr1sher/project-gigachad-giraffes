import unittest
from peewee import *

from app import TimelinePost, get_time_line_post

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe',
        email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe',
        email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2

        #TODO: Get timeline posts and assert that they are correct
        #Check that second post comes before first post
        posts = get_time_line_post()["timeline_posts"]
        assert posts[0]['id'] == 2
        assert posts[0]['name'] == 'Jane Doe'
        assert posts[0]['email'] == 'jane@example.com'
        assert posts[0]['content'] == 'Hello world, I\'m Jane!'

        assert posts[1]['id'] == 1
        assert posts[1]['name'] == 'John Doe'
        assert posts[1]['email'] == 'john@example.com'
        assert posts[1]['content'] == 'Hello world, I\'m John!'
    