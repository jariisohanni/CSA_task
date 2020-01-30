import pytest

from app import main

def test_setup():
    assert( main.testOK() == True)
