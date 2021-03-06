import os
import tempfile

import pytest

from PythonAnywhereFlaskTest1 import create_app



@pytest.fixture
def app():
    app = create_app({"TESTING": True})
#    print(app)
    yield app



@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
