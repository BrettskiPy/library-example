import pytest
from main import storage


# Define the fixture for initializing the database
@pytest.fixture(autouse=True)
def setup_storage():
    storage.clear()
    storage.extend(
        [
            {"title": "Book 1", "author": "Author 1", "year": 2000},
            {"title": "Book 2", "author": "Author 2", "year": 2001},
            {"title": "Book 3", "author": "Author 3", "year": 2002},
        ]
    )
