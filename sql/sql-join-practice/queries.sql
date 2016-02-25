-- 1. What are the top 50 worst rated movies? The results should
-- include the movie title and rating and be sorted by the worst
-- rating first.

SELECT title,
       rating
FROM movies
ORDER BY rating LIMIT 50;

 -- 2. What movies do not have a rating? The results should include
-- just the movie titles in sorted order.

SELECT title
FROM movies
WHERE rating IS NULL
ORDER BY title;

 -- 3. What movies have the word "thrilling" in their synopsis? The
-- results should just include the movie title.

SELECT title
FROM movies
WHERE synopsis ILIKE '%thrilling%'
ORDER BY title;

 -- 4. What were the highest rated 'Science Fiction & Fantasy' movies
-- released in the 80's? The results should include the movie title,
-- the year released, and rating sorted by highest rating first.

SELECT title,
       YEAR,
       rating
FROM movies
WHERE genre_id = 17
  AND YEAR > 1979
  AND YEAR < 1990
ORDER BY YEAR;

 -- 5. What actors have starred as James Bond? The results should
-- include the actor name, movie title, year released, and be sorted
-- by year in ascending order (earliest year appears first).

SELECT actors.name,
       movies.title,
       movies.YEAR
FROM cast_members
JOIN actors ON cast_members.actor_id = actors.id
JOIN movies ON cast_members.movie_id = movies.id
WHERE cast_members.character = 'James Bond'
ORDER BY movies.YEAR;

 -- 6. What movies has Julianne Moore starred in? The results should
-- include the movie title, year released, and name of the genre,
-- sorted by genre first and then movie title.

SELECT genres.name,
       movies.title,
       movies.YEAR
FROM cast_members
JOIN actors ON cast_members.actor_id = actors.id
JOIN movies ON cast_members.movie_id = movies.id
JOIN genres ON movies.genre_id = genres.id
WHERE actors.name = 'Julianne Moore'
ORDER BY genres.name,
         movies.title;

 -- 7. What were the five earliest horror movies and what studios
-- produced them? Include the movie title, year released, and studio
-- name (if any) in the results sorted by year.

SELECT movies.title,
       movies.YEAR,
              studios.name
FROM movies
LEFT OUTER JOIN studios ON movies.studio_id = studios.id
JOIN genres ON movies.genre_id = genres.id
WHERE genres.name = 'Horror'
ORDER BY movies.YEAR LIMIT 5;

