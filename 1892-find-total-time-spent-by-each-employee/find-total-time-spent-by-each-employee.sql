SELECT event_day AS day, emp_id, SUM(out_time) - SUM(in_time) AS total_time 
FROM Employees e
GROUP BY day, emp_id

# 00:02