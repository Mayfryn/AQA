import pytest
import pytest as pytest
import Homework5.hometask53
from Lesson5.my_class1 import User


@pytest.fixture()
def user():
    fixture = User(name='Roman', age=30)
    return fixture

def test_user(user):
    assert user.name == 'Roman'