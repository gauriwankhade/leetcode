# Write your MySQL query statement below

select p.firstName, p.lastName, a.city, a.state FROM Person AS p left join Address AS a ON
p.personId = a.personId ;

