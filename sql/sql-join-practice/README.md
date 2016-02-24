# SQL Join Practice

Do this in pairs!

## Objectives

Write SQL queries that:
  - filter, order, and limit the number of results shown
  - pull information from multiple tables.

## Instructions

For this challenge you'll need to write queries against a database containing movie information. A snapshot of the database is provided in the *movie_database.sql* file which can be recreated with the following commands:

```sh
$ dropdb movies
$ createdb movies
$ psql movies < movie_database.sql
```

Once these commands have finished running, use the `psql movies` command to verify the database has been populated:

```sh
$ psql movies

movies=# SELECT count(*) FROM movies;
 count
-------
  3546
(1 row)
```

Once you've verified that your database contains information, write queries to answer the following questions, adding each query to a new file called *queries.sql*:

1. What are the top 50 worst rated movies? The results should include the movie title and rating and be sorted by the worst rating first.
1. What movies do not have a rating? The results should include just the movie titles in sorted order.
1. What movies have the word "thrilling" in their synopsis? The results should just include the movie title.
1. What were the highest rated 'Science Fiction & Fantasy' movies released in the 80's? The results should include the movie title, the year released, and rating sorted by highest rating first.
1. What actors have starred as James Bond? The results should include the actor name, movie title, year released, and be sorted by year in ascending order (earliest year appears first).
1. What movies has Julianne Moore starred in? The results should include the movie title, year released, and name of the genre, sorted by genre first and then movie title.
1. What were the five earliest horror movies and what studios produced them? Include the movie title, year released, and studio name (if any) in the results sorted by year.
