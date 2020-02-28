/*
## Questions

### 620. [Not Boring Movies](https://leetcode.com/problems/not-boring-movies/)

SQL Schema >
Create table If Not Exists cinema (id int, movie varchar(255), description varchar(255), rating float(2, 1))
Truncate table cinema
insert into cinema (id, movie, description, rating) values ('1', 'War', 'great 3D', '8.9')
insert into cinema (id, movie, description, rating) values ('2', 'Science', 'fiction', '8.5')
insert into cinema (id, movie, description, rating) values ('3', 'irish', 'boring', '6.2')
insert into cinema (id, movie, description, rating) values ('4', 'Ice song', 'Fantacy', '8.6')
insert into cinema (id, movie, description, rating) values ('5', 'House card', 'Interesting', '9.1')

X city opened a new cinema, many people would like to go to this cinema. The cinema also gives out a poster indicating the movies’ ratings and descriptions.
Please write a SQL query to output movies with an odd numbered ID and a description that is not 'boring'. Order the result by rating.



For example, table cinema:

+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+
For the example above, the output should be:
+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   5     | House card|   Interesting|   9.1     |
|   1     | War       |   great 3D   |   8.9     |
+---------+-----------+--------------+-----------+
+---------------------+

Solutions

*/

-- Write your MySQL query statement below

SELECT id,movie,description,rating
FROM cinema
GROUP BY rating
HAVING (id%2 = 1 AND description != "boring")
ORDER BY rating DESC;


-- Runtime : 223 ms, faster than 68.89% of MySQL online submissions
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions
-- MySQL


-- Solution : 2

-- Write your MySQL query statement below

SELECT *
FROM cinema
WHERE (id%2 = 1 AND description NOT LIKE "boring")
ORDER BY rating DESC;


-- Runtime : 131 ms, faster than 94.32% of MySQL online submissions
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions
-- MySQL