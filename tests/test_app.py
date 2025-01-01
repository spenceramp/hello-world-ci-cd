import unittest
from app import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # Create a test client for the Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        # Test the '/' route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Welcome!')

    def test_custom_route(self):
        # Test the '/how are you' route
        response = self.app.get('/how are you')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'I am good, how about you?')


if __name__ == '__main__':
    unittest.main()
