# Sketch FastAPI-SQLModel-Alembic CDS

## Introduction
This repository was made as a study case for usage of FastAPI with [SQLModel](https://sqlmodel.tiangolo.com/) (a high-level wrapper for [SQLAlchemy](https://docs.sqlalchemy.org/) with a lot of [Pydantic](https://pydantic-docs.helpmanual.io)) and Alembic (a SQLAlchemy-native database migration tool).

### Why?
The CDS will essentially be a data service, heavily using SQL databases and having an API interface and, to start, I had medium experience with FastAPI's inner workings and little to none with SQLAlchemy. When I found out about SQLModel and how it kind of unites both, it seemed like a good opportunity to take the opportunity to learn and see how much easier it is to write than SQLAlchemy (which can have some quite heavy, non-pythonic syntax. SQLModel could allegedly improve overall code readability, so I tried it out.

### How?
I started with all "Getting Started" tutorials for each and built from there. SQLModel is quite new, currently at version **0.0.6** (!), and does not have a lot of innate functionality as of yet, so you can easily go coding through with the documentation for it in around 6-8 hours. It won't do almost anything more than what SQLAlchemy and Pydantic can already do, but it offers a **much** nicer syntax by wrapping them together.

FastAPI's documentation can be a bit bigger, but I started minimal here. I still want to see what are some ways we can make better use of its features.

I also tried to completely avoid native SQLAlchemy dialect altogether. Avoiding the double dialect improves readability and lowers the bar for understanding the code. Furthermore, as SQLModel is a wrapper on top of SQLAlchemy, there's *just no reason* to use SQLAlchemy when there is a top-level SQLModel dialect alternative.

### We already have a `centralized_data_service` repo. So, again, why?

This is not an attempt to completely substitute the `centralized_data_service` repository, but to offer a side view on a possibly cleaner version of it. I went all the way from 0 to develop this with the most up-to-date original documentation. What I want is to take your suggestions on what can be improved on this and also to have you take a look at some improvements that can be taken from here as well. I will then start submitting my PR's to `centralized_data_service`.

## Structure
I'll be frank and say that I didn't give much attention to the current `centralized_data_service` repository to build this one, mainly because I felt I wouldn't learn it well by doing it that way - I could kinda just go with what's written and keep reproducing code without understanding it. I took entirely upon me this weekend that I would learn the shit out of this and I did :smile:

So, here's the overall structure of this repo:

```
alembic/ -> this module manages database migration related stuff
         -> it does NOT have anything to do with data serving, so outside `cds` module
├── versions/ -> revision (migration) code itself
│   └── ...
├── env.py -> defines a few important environment settings for Alembic, such as database connection
└── script.py.mako -> template revision file, used to generate revision code

cds/ -> this module manages the actual data serving through the API
     -> **this also does NOT have anything to do with database migrations**
├── api/ -> contains most, if not all, FastAPI-related data serving code
│   ├── routes/ -> route hierarchy (e.g. /v1/, /dveloper/, /challenge/)
│   │   └── ...
│   ├── openapi.py
│   ├── middleware.py
│   └── ...
├── database/ -> database connection stuff
│   └── config.py
├── schema/ -> defines all data models, SQL-bound or not
│   ├── models/ -> SQL-unbound models (e.g. table=False)
│   │   └── ...
│   └── tables/ -> SQL-bound models (e.g. table=True)
│       └── ...
├── settings/ -> holds environment and other common variables
│   ├── environment.py
│   └── globals.py
└── main.py -> entry point
.gitignore
alembic.ini -> alembic configuration file
README.md
requirements.txt -> to be installed with pip install -r requirements.txt (we can use poetry too)

(and maybe some .env files if you like)
```

> Note that, although the `alembic` and `cds` modules are separated for having different functions altogether, `alembic` makes use of the [**SQL metadata**](https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#sqlmodel-metadata) generated in the CDS to run revision generations by comparing it against the current state of the database. This is why they have to be maintained in the same repository.

## Setting up
First, `pip install -r requirements.txt`. Note that SQLAlchemy library introduced some breaking change to SQLModel in version 1.46.0, so we're using 1.45.0.

### Database
Secondly, get a MySQL database rolling somewhere so you can start testing migrations. I installed it on my own machine without Docker, but you could use it if you want. Create a database and name it `cds`:
```sql
CREATE DATABASE cds;
```
Set your database environment variables as required in `cds/settings/environment.py` and, from the MySQL perspective, you're done. All DDL will be done through **Alembic**.

Now that you have everything set up, do:
```bash
alembic upgrade head
```
This will apply all database migrations. If everything runs correctly, you should be able to see three new tables in your MySQL database:
- `developer`
- `challenge`
- `developer_mcq_score`

Now, add some testing rows in these tables manually (using some software such as DBeaver).

### Data Service
Now, run the service with:
```bash
uvicorn cds.main:app --port 8000 (optionally include --reload)
```

You should be able to query data from it already. Try these:
- GET `http://localhost:8000/developer`
- GET `http://localhost:8000/challenge`
- GET `http://localhost:8000/developer/1/`
- GET `http://localhost:8000/developer/1/challenge`
- GET `http://localhost:8000/developer/1/challenge/1`

If you included at least one row in each table with `id`s 1, you should already be seeing some results.

## Finally

At this point, I just highly encourage you to go through the code, since this is not meant to be the CDS itself or anything. I've tried my best to keep it short and well-structured, with no big files at all. It should be fairly easy to read, and you should notice some design patterns in there that I felt enforced better concern separations.

I'll point out a few special points:
- How table models are separated from table models and why
    - Also how having "Read" models can reduce bandwidth usage and enforce better schema
- How `SQLModel.metadata` informs Alembic what the structure of the database should be
    - Especially how all the **table models have to be imported after SQLModel** to be included
- How straightforward the actual API path operation code is!

## Outro
I had a lot of fun doing this. Really hope this helps bootstrap the CDS with a bit more context in place :)
