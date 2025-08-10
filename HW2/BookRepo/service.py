from models import Book
from repo import BookRepo


class BookService:

    def __init__(self, book_repo: BookRepo):
        self.book_repo = book_repo


    async def add_book(self, user_id: int, title: str, pages_count: int) -> Book:
        if pages_count < 0:
            raise ValueError("введено неверное количество страниц")


        book = self.book_repo.create_book(user_id, title, pages_count)
        return book

    async def increase_read_pages(self, user_id: int, title: str, pages: int) -> None:
        self.book_repo.update_pages(user_id, pages, title)

    async def list_books(self, user_id: int) -> list[Book]:
        self.book_repo.fetch_books(user_id)

    async def remove_book(self, user_id: int, title: str) -> None:
        self.book_repo.delete_book(user_id, title)
