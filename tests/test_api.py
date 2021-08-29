import unittest
from wsgi import app


class TestBubbleSortApi(unittest.TestCase):

    # setup test flask test client
    def setUp(self):
        self.client = app.test_client()

    # helper function for making requests
    def post(self, request):
        return self.client.post('api/v1/bubble', json=request)

    def test_for_empty_list(self):

        """ testing for empty list """

        app.config['MAXIMUM_LENGTH'] = 2
        response = self.post({"unsorted-list": []})
        self.assertEqual(response.json, {'message': 'Must not be empty'})
        self.assertEqual(response.status_code, 401)

    def test_for_max_length(self):

        """testing if the length exception works"""

        app.config['MAXIMUM_LENGTH'] = 2
        response = self.post({"unsorted-list": [6, 2, [4, 3], [[[5], None], 1]]})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'error': 'ValueError',
                                         'message': 'Elements in list must be less then Max Length'})

    def test_sort_api(self):

        """testing post request"""

        app.config['MAXIMUM_LENGTH'] = 10
        response = self.post({"unsorted-list": [6, 2, [4, 3], [[[5], None], 1]]})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'sorted-list': [1, 2, 3, 4, 5, 6]})
