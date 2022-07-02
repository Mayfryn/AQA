import unittest
import requests
 

class TestBooks(unittest.TestCase):

    def test_book_create_positive(self):
        host = "pulse-rest-testing.herokuapp.com"
        res = "books"
        book_data = {"title": "War and Peace", "author": "Levko Debeluj"}
        resp = requests.post(f"https://{host}/{res}", data=book_data)
        self.assertEqual(201, resp.status_code)
        book_body = resp.json()
        self.assertIn("id", book_body.keys())
        self.assertEqual("War and Peace", book_body["title"])
        self.assertEqual("Levko Debeluj", book_body["author"])

    if __name__ == '__main':
        unittest.main()
