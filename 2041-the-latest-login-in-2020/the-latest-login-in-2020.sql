SELECT user_id, MAX(time_stamp) last_stamp
FROM Logins
WHERE EXTRACT(YEAR FROM time_stamp) = 2020
GROUP BY user_id;

# 00:08