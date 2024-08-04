import typing
import strawberry
from queryFields import book, books, author, authors
from entityTypes import Book, Author


@strawberry.type
class Query:
    book: Book | None = strawberry.field(resolver=book)
    books: typing.List[Book] | None = strawberry.field(resolver=books)
    author: Author | None = strawberry.field(resolver=author)
    authors: typing.List[Author] | None = strawberry.field(resolver=authors)


schema = strawberry.Schema(query=Query)
