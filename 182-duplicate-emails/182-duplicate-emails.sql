# Write your MySQL query statement below


SELECT
    DISTINCT a.email AS Email
FROM 
    Person AS a
INNER JOIN 
    Person AS p
ON
    p.email = a.email AND p.id != a.id;
