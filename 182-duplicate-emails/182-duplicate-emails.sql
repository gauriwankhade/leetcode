# Write your MySQL query statement below


SELECT
    DISTINCT a.email AS Email
FROM 
    Person AS a
WHERE (select count(*) FROM Person AS p WHERE p.email = a.email) > 1;