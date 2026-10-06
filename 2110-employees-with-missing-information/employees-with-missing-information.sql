(
    SELECT employee_id
    FROM Salaries

    EXCEPT

    SELECT employee_id
    FROM Employees
)

UNION

(
    SELECT employee_id
    FROM Employees

    EXCEPT

    SELECT employee_id
    FROM Salaries
)
ORDER BY employee_id;

# 00:12
