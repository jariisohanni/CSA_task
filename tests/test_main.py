import pytest
import string
import random

from app import main
from app.encryption import encryption_engine
from app.users.user_manager import UserManager
from app.users.user import User


def test_setup():
    assert (main.testOK() == True)


def test_user_manager():
    um = UserManager()
    um.addUser(User("jari", "testi"))
    assert (um.find_user_with_id("jari") is not None)
    assert (um.find_user_with_id("joni") is not None)

def test_hash():
    test_count = 1
    max_test = 100
    match_found = False
    while test_count <= max_test:
        p1 = randomString(10)
        p2 = randomString(11)
        sha1 = encryption_engine.hash_text(p1)
        sha2 = encryption_engine.hash_text(p2)
        if sha1 == sha2:
            match_found = True

        test_count += 1

    assert (False == match_found)


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
