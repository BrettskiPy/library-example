from fastapi.testclient import TestClient
from main import app, storage
import pytest

client = TestClient(app)


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


# Test for creating a new book
def test_create_book():
    response = client.post(
        "/books/", json={"title": "New Book", "author": "New Author", "year": 2023}
    )
    assert response.status_code == 200
    assert response.json() == {
        "title": "New Book",
        "author": "New Author",
        "year": 2023,
    }


# Test for reading books
def test_read_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) == 3


# Test for reading a single book
def test_read_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Book 2"


# Test for updating a book
def test_update_book():
    response = client.put(
        "/books/1",
        json={"title": "Updated Book", "author": "Updated Author", "year": 2023},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Book"


# Test for deleting a book
def test_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 200
    follow_up_response = client.get("/books/")
    assert len(follow_up_response.json()) == 2
