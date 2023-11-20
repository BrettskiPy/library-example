# Library CRUD Example App
An example FastAPI CRUD application.

![Alt text](library.png)
This is an example book CRUD (Create, Read, Update, Delete) application built with FastAPI and Pydantic. It allows you to manage an books performing various operations. This application also includes tests using Pytest.

## Features
- **Create Book**: Add a new book to the collection.
- **Read Books**: Retrieve a list of all books or a specific book by its ID.
- **Update Book**: Modify details of an existing book.
- **Delete Book**: Remove a book from the collection.

## Requirements
- FastAPI
- Pydantic
- Uvicorn (for running the server)

## Installation
```
pip install -r requirements.txt
```

## Running the Application
```
uvicorn main:app --reload
```

## API Endpoints
- `POST /books/` Add a new book. Requires a JSON body with `title`, `author`, and `year`.
- `GET /books/` Retrieve all books. Optional query parameter `limit` to limit the number of books returned.
- `GET /books/{book_id}` Retrieve a book by its ID.
- `PUT /books/{book_id}` Update a book by its ID. Requires a JSON body with updated `title`, `author`, and `year`.
- `DELETE /books/{book_id}` Delete a book by its ID.

## Data Model
### Book
- `title`: string
- `author`: string
- `year`: integer

## Error Handling
- Returns a 404 error if a book with the specified ID is not found.

## Curl Examples
### Adding a book
```
curl -X 'POST' \
  'http://127.0.0.1:8000/books/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "year": 1925
}'
```
### Retrieving Books
```
curl -X 'GET' \
  'http://127.0.0.1:8000/books/' \
  -H 'accept: application/json'
```
With a limit
```
curl -X 'GET' \
  'http://127.0.0.1:8000/books/?limit=2' \
  -H 'accept: application/json'
```
### Retrieving Book By ID
```
curl -X 'GET' \
  'http://127.0.0.1:8000/books/{book_id}' \
  -H 'accept: application/json'
```
### Updating a Book
```
curl -X 'PUT' \
  'http://127.0.0.1:8000/books/{book_id}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "New Title",
  "author": "New Author",
  "year": 1926
}'
```
### Deleting a Book
```
curl -X 'DELETE' \
  'http://127.0.0.1:8000/books/{book_id}' \
  -H 'accept: application/json'
```
