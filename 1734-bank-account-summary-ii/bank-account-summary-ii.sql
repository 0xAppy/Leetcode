SELECT u.name, SUM(t.amount) balance
FROM Transactions t
JOIN Users u
ON u.account = t.account
GROUP BY u.account
HAVING SUM(t.amount) > 10000;

# 00:07