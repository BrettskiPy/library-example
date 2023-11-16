from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Mock database to store books
storage = []


# Pydantic model for Book
class Book(BaseModel):
    title: str
    author: str
    year: int


# CRUD operations
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    storage.append(book)
    return book


@app.get("/books/", response_model=List[Book])
def read_books(limit: int = None):
    if limit:
        return storage[:limit]
    else:
        return storage


@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    if book_id < 0 or book_id >= len(storage):
        raise HTTPException(status_code=404, detail="Book not found")
    return storage[book_id]


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    if book_id < 0 or book_id >= len(storage):
        raise HTTPException(status_code=404, detail="Book not found")
    storage[book_id] = updated_book
    return updated_book


@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    if book_id < 0 or book_id >= len(storage):
        raise HTTPException(status_code=404, detail="Book not found")
    deleted_book = storage.pop(book_id)
    return deleted_book
