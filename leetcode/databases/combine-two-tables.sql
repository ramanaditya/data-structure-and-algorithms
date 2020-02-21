/*
## Questions

### 175. [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)

SQL Schema

Create table Person (PersonId int, FirstName varchar(255), LastName varchar(255))
Create table Address (AddressId int, PersonId int, City varchar(255), State varchar(255))
Truncate table Person
insert into Person (PersonId, LastName, FirstName) values ('1', 'Wang', 'Allen')
Truncate table Address
insert into Address (AddressId, PersonId, City, State) values ('1', '2', 'New York City', 'New York')

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.


Write a SQL query for a report that provides the following information for each person in the Person table,
regardless if there is an address for each of those people:

FirstName, LastName, City, State

Solutions

*/

-- Write your MySQL query statement below

SELECT P.FirstName, P.LastName, A.City, A.State
FROM Person P
LEFT JOIN Address A ON P.PersonId=A.PersonId;


-- Runtime : 358 ms, faster than 73.98% of MySQL online submissions
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions
-- MySQL