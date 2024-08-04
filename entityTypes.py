import typing
import strawberry
from utils.processQuery import (
    singleRowQueryAndMap,
    singleRowQueryAndTransform,
    multiRowQueryAndTransform,
)


def authorForBook(root: "Book") -> "Author":
    id = root.id
    query = f"select author_id from graphqltest.books where book_id={id};"
    res = singleRowQueryAndMap(query, ["author_id"])
    print(res)
    if not res:
        return None
    author_id = res["author_id"]

    query = f"select author_id, name, email, city from graphqltest.authors where author_id={author_id};"
    query += ";"
    return singleRowQueryAndTransform(
        query,
        ["author_id", "name", "email", "city"],
        Author,
        {"author_id": "id", "name": "name", "email": "email", "city": "city"},
    )


def booksForAuthor(root: "Author") -> typing.List["Book"]:
    if not root.id:
        return []
    query = f"select book_id, title, author_id from graphqltest.books where author_id={root.id};"
    return multiRowQueryAndTransform(
        query,
        ["book_id", "title", "author_id"],
        Book,
        {"book_id": "id", "title": "title"},
    )


@strawberry.type
class Book:
    def __init__(self, d=None):
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)

    id: int
    title: str
    author: "Author" = strawberry.field(resolver=authorForBook)


@strawberry.type
class Author:
    def __init__(self, d=None):
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)

    id: int
    name: str
    city: str
    email: str
    books: typing.List[Book] = strawberry.field(resolver=booksForAuthor)
