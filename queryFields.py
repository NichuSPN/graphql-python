import typing
from entityTypes import Book, Author
from utils.processQuery import singleRowQueryAndTransform, multiRowQueryAndTransform


def book(id: int) -> Book | None:
    query = (
        f"select book_id, title, author_id from graphqltest.books where book_id={id};"
    )
    return singleRowQueryAndTransform(
        query,
        ["book_id", "title", "author_id"],
        Book,
        {"book_id": "id", "title": "title"},
    )


def books(
    limit: typing.Optional[int] = None, offset: typing.Optional[int] = None
) -> typing.List[Book] | None:
    query = "select book_id, title, author_id from graphqltest.books"
    if limit:
        query += f" limit {limit}"
    if offset:
        query += f" offset {offset}"
    query += ";"
    return multiRowQueryAndTransform(
        query,
        ["book_id", "title", "author_id"],
        Book,
        {"book_id": "id", "title": "title"},
    )


def author(id: int) -> Author | None:
    query = f"select author_id, name, email, city from graphqltest.authors where author_id={id};"
    query += ";"
    return singleRowQueryAndTransform(
        query,
        ["author_id", "name", "email", "city"],
        Author,
        {"author_id": "id", "name": "name", "email": "email", "city": "city"},
    )


def authors(
    limit: typing.Optional[int] = None, offset: typing.Optional[int] = None
) -> typing.List[Author] | None:
    query = "select author_id, name, email, city from graphqltest.authors"
    if limit:
        query += f" limit {limit}"
    if offset:
        query += f" offset {offset}"
    query += ";"
    return multiRowQueryAndTransform(
        query,
        ["author_id", "name", "email", "city"],
        Author,
        {"author_id": "id", "name": "name", "email": "email", "city": "city"},
    )
