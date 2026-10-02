SELECT 
    stock_name,
    SUM(
        CASE
            WHEN operation = 'SELL' THEN price
            WHEN operation = 'BUY' THEN -price
        END
    ) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;

# 00:13