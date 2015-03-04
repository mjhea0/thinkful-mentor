import unittest
import os
import json
from urlparse import urlparse

# Configure our app to use the testing databse
os.environ["CONFIG_PATH"] = "posts.config.TestingConfig"

from posts import app
from posts import models
from posts.database import Base, engine, session


class TestAPI(unittest.TestCase):
    """ Tests for the posts API """

    def setUp(self):
        """ Test setup """
        self.client = app.test_client()

        # Set up the tables in the database
        Base.metadata.create_all(engine)

    def tearDown(self):
        """ Test teardown """
        session.close()
        # Remove the tables and their data from the database
        Base.metadata.drop_all(engine)

    def test_get_empty_posts(self):
        """ Getting posts from an empty database """
        response = self.client.get(
            "/api/posts",
            headers=[("Accept", "application/json")])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/json")

        data = json.loads(response.data)
        self.assertEqual(data, [])

    def test_get_posts(self):
        """ Getting posts from a populated database """
        postA = models.Post(title="Example Post A", body="Just a test")
        postB = models.Post(title="Example Post B", body="Still a test")

        session.add_all([postA, postB])
        session.commit()

        response = self.client.get(
            "/api/posts", headers=[("Accept", "application/json")])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/json")

        data = json.loads(response.data)
        self.assertEqual(len(data), 2)

        postA = data[0]
        self.assertEqual(postA["title"], "Example Post A")
        self.assertEqual(postA["body"], "Just a test")

        postB = data[1]
        self.assertEqual(postB["title"], "Example Post B")
        self.assertEqual(postB["body"], "Still a test")

    def test_get_single_post(self):
        """ Getting a single post from a populated database"""
        postA = models.Post(title="Example Post A", body="Just a test")
        postB = models.Post(title="Example Post B", body="Still a test")

        session.add_all([postA, postB])
        session.commit()

        response = self.client.get(
            "/api/posts/{}".format(postB.id),
            headers=[("Accept", "application/json")])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/json")

        post = json.loads(response.data)
        self.assertEqual(post["title"], "Example Post B")
        self.assertEqual(post["body"], "Still a test")

    def test_get_non_existent_post(self):
        """ Getting a single post which doesn't exist """
        response = self.client.get(
            "/api/posts/1", headers=[("Accept", "application/json")])

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.mimetype, "application/json")

        data = json.loads(response.data)
        self.assertEqual(data["message"], "Could not find post with id 1")

    def test_unsupported_accept_header(self):
        response = self.client.get(
            "/api/posts", headers=[("Accept", "application/xml")])

        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.mimetype, "application/json")

        data = json.loads(response.data)
        self.assertEqual(
            data["message"], "Request must accept application/json data")

    def test_delete_single_post(self):
        postA = models.Post(title="Example Post A", body="Delete this")
        postB = models.Post(title="Example Post B", body="Don't delete this")

        session.add_all([postA, postB])
        session.commit()

        response = self.client.get(
            "/api/posts/{}".format(postA.id),
            headers=[("Accept", "application/json")])

        session.delete(postA)
        session.commit()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/json")

        # data = json.loads(response.data)

        posts = session.query(models.Post).all()
        self.assertEqual(len(posts), 1)

        postB = posts[0]
        self.assertEqual(postB.title, "Example Post B")
        self.assertEqual(postB.body, "Don't delete this")
        # find a way to assert postA is not in posts

    def test_get_posts_with_title_and_body(self):
        """ Filtering posts by title and body """
        postA = models.Post(title="Post with bells", body="Just a test")
        postB = models.Post(title="Post with whistles", body="Still a test")
        postC = models.Post(
            title="Post with bells and whistles", body="Another test")

        session.add_all([postA, postB, postC])
        session.commit()

        response = self.client.get(
            "/api/posts?title_like=whistles&body_like=Still",
            headers=[("Accept", "application/json")])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/json")

        posts = json.loads(response.data)
        self.assertEqual(len(posts), 1)

        post = posts[0]
        self.assertEqual(post["title"], "Post with whistles")
        self.assertEqual(post["body"], "Still a test")

        # add this test if only testing title, not body
        # post = posts[1]
        # self.assertEqual(post["title"], "Post with bells and whistles")
        # self.assertEqual(post["body"], "Another test")

    def test_post_post(self):
        """ Posting a new post """
        data = {
            "title": "Example Post",
            "body": "Just a test"
            }

        response = self.client.post(
            "/api/posts",
            data=json.dumps(data),
            content_type="application/json",
            headers=[("Accept", "application/json")]
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.mimetype, "application/json")
        self.assertEqual(
            urlparse(response.headers.get("Location")).path, "/api/posts/1")

        data = json.loads(response.data)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["title"], "Example Post")
        self.assertEqual(data["body"], "Just a test")

        posts = session.query(models.Post).all()
        self.assertEqual(len(posts), 1)

        post = posts[0]
        self.assertEqual(post.title, "Example Post")
        self.assertEqual(post.body, "Just a test")

    def test_unsupported_mimetype(self):
        data = "<xml></xml>"
        response = self.client.post(
            "/api/posts",
            data=json.dumps(data),
            content_type="application/xml",
            headers=[("Accept", "application/json")]
        )

        self.assertEqual(response.status_code, 415)
        self.assertEqual(response.mimetype, "application/json")

        data = json.loads(response.data)
        self.assertEqual(
            data["message"], "Request must contain application/json data")

    def test_invalid_data(self):
        """ Posting a post with an invalid body """
        data = {
            "title": "Example Post",
            "body": 32
            }

        response = self.client.post(
            "/api/posts",
            data=json.dumps(data),
            content_type="application/json",
            headers=[("Accept", "application/json")]
        )

        self.assertEqual(response.status_code, 422)

        data = json.loads(response.data)
        self.assertEqual(data["message"], "32 is not of type 'string'")

    def test_missing_data(self):
        """ Posting a post with a missing body """
        data = {
            "title": "Example Post",
        }

        response = self.client.post(
            "/api/posts",
            data=json.dumps(data),
            content_type="application/json",
            headers=[("Accept", "application/json")]
        )

        self.assertEqual(response.status_code, 422)

        data = json.loads(response.data)
        self.assertEqual(data["message"], "'body' is a required property")

    def test_update_post(self):
        """ Updating a post (PUT request) from a populated database """
        postA = models.Post(title="Example Post A", body="Just a test")
        # postB = models.Post(title="Example Post B", body="Still a test")

        session.add(postA)
        session.commit()

        data_payload = {
            "title": "Example Post",
            "body": "a new test"
            }

        response = self.client.put("/api/posts/{}".format(postA.id),
                                   data=json.dumps(data_payload),
                                   content_type="application/json",
                                   headers=[("Accept", "application/json")]
                                   )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/json")

        data_response = json.loads(response.data)
        # {u'body': u'Just a test', u'id': 1, u'title': u'Example Post'}
        self.assertEqual(len(data_response), 3)

        # postA = data[0]
        self.assertEqual(data_response["title"], "Example Post")
        self.assertEqual(data_response["body"], "a new test")

    # additional tests for the update_post endpoint

    def test_update_nonexistent_post(self):
        """ Attempting to update a post that does not exist"""
        data_payload = {
            "title": "Example Post",
            "body": "this post does not already exist"
            }

        response = self.client.put("/api/posts/{}".format(1),
                                   data=json.dumps(data_payload),
                                   content_type="application/json",
                                   headers=[("Accept", "application/json")]
                                   )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.mimetype, "application/json")

        data = json.loads(response.data)
        self.assertEqual(
            data["message"], "Could not find post with id {}".format(1))

    def test_update_post_with_invalid_json(self):
        """ Attempting to update an existing post with invalid JSON"""
        postA = models.Post(
            title="Example Post A", body="this will be valid JSON")

        session.add(postA)
        session.commit()

        data_payload = {
            "title": "Example Post",
            "body": 32
            }

        response = self.client.put("/api/posts/{}".format(postA.id),
                                   data=json.dumps(data_payload),
                                   content_type="application/json",
                                   headers=[("Accept", "application/json")]
                                   )

        self.assertEqual(response.status_code, 422)

        data = json.loads(response.data)
        self.assertEqual(data["message"], "32 is not of type 'string'")

    def test_update_post_with_missing_data(self):
        """ Attempting to update a post with missing data (title or body)"""
        postA = models.Post(title="Example Post A", body="Just a test")

        session.add(postA)
        session.commit()

        data_payload = {
            "title": "Example Post"
        }

        response = self.client.put("/api/posts/{}".format(postA.id),
                                   data=json.dumps(data_payload),
                                   content_type="application/json",
                                   headers=[("Accept", "application/json")]
                                   )

        self.assertEqual(response.status_code, 422)

        data = json.loads(response.data)
        self.assertEqual(data["message"], "'body' is a required property")

if __name__ == "__main__":
    unittest.main()
