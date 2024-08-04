# QraphQL basic implementation using Python 3
This repository is part of my learning to create GraphQL APIs using Python. For this, I am using the example that the strawberry library that I am using has already used. It is organizing Books and Authors. It is a straightforward relation where each author can have multiple books in their name and each book should have an author.
To have actual data to test, we use Postgres.

## Prerequisites
- Python 3.7+ (I used Python 3.10)
- PostgreSQL with psql


## Setup
- First, clone the repository
- Go into graphql-python folder using `cd graphql-python`
- Connect to your database using `psql`
- Do `\i bookAuthor.sql` and the required tables will be created
- Add data to the table as required 
- Exit the psql terminal
- Create a `.env` file in the root folder and update the credentials of the database
- To install dependencies run `pip install -r requirements.txt`
- To start the server run `strawberry server schema`
- We can see the graphql playground in http://0.0.0.0:8000/graphql
