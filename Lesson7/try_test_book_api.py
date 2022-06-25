import requests
import pytest

book_data_llist = [
    {"title": "War and Peace", "author": "Levko Debeluj"},
    {"title": "5468y74589", "author": "245624"},
    {"title": "^%T&%", "author": "4325646"}
]


@pytest.mark.parametrize("book_data", book_data_llist)
def test_book_create_positive(baseurl, delete_created_book, book_data):
    resource = "books/"
    resp = requests.post(baseurl + resource, data=book_data)

    host = "pulse-rest-testing.herokuapp.com"

    resp = requests.post(f"https://{host}/{res}", data=book_data)
