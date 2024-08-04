create schema graphqltest;

create table graphqltest.books(book_id bigserial unique, title text, author_id bigint, primary key(title, author_id));

create table graphqltest.authors(author_id bigserial unique, name text, city text, email text, primary key(name, email));

alter table graphqltest.books add constraint books_author foreign key (author_id) references graphqltest.authors(author_id);