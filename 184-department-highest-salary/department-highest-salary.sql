WITH RANKED AS (
    SELECT 
        d.name Department, 
        e.name Employee, 
        e.salary Salary,
        DENSE_RANK() OVER(PARTITION BY d.id ORDER BY e.salary DESC) rnk
    FROM Employee e
    JOIN Department d
    ON e.departmentId = d.id
)

SELECT Department, Employee, Salary
FROM ranked
WHERE rnk = 1;

# 00:16
