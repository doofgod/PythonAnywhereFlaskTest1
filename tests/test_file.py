import pytest


def test_math(client):
    assert 1==1
    assert 1+2 ==3

def test_math_fail(client):
    assert 2==2

def test_hello_world(client):
    response = client.get("/hello/")
    assert b"Hello, World" in response.data
