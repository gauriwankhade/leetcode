# Write your MySQL query statement below

# select e.name AS Employee from Employee AS e WHERE
# e.salary > (select m.salary FROM Employee AS m WHERE m.id =  e.managerId);




SELECT
    e.name AS Employee

FROM
    Employee AS e,
    Employee AS m
WHERE
    e.ManagerId = m.id AND
    e.salary > m.salary;
    
