-- Top Profitability Conditions

SELECT
    Traffic_Level,
    Weather,
    ROUND(AVG(Profit), 2) AS avg_profit,
    ROUND(AVG(Delivery_Time_min), 2) AS avg_delivery_time
FROM food_delivery
GROUP BY Traffic_Level, Weather
ORDER BY avg_profit DESC;


-- This answers:
-- Which operational conditions are most profitable?
-- Which combinations are operationally expensive?

-- Vehicle Performance

SELECT
    Vehicle_Type,
    ROUND(AVG(Delivery_Time_min), 2) AS avg_delivery_time,
    ROUND(AVG(Profit), 2) AS avg_profit
FROM food_delivery
GROUP BY Vehicle_Type
ORDER BY avg_profit DESC;

-- Think:
-- Which vehicles should the company prioritize?
-- Which fleet type is most profitable?

-- Peak Hour Performance

SELECT
    Peak_Hour,
    COUNT(*) AS total_orders,
    ROUND(AVG(Delivery_Time_min), 2) AS avg_delivery_time,
    ROUND(AVG(Profit), 2) AS avg_profit
FROM food_delivery
GROUP BY Peak_Hour;

-- Question:
-- Are peak-hour operations profitable enough to justify operational strain?

-- Courier Efficiency

SELECT
    Courier_Experience_yrs,
    ROUND(AVG(Delivery_Time_min), 2) AS avg_delivery_time,
    ROUND(AVG(Profit), 2) AS avg_profit
FROM food_delivery
GROUP BY Courier_Experience_yrs
ORDER BY Courier_Experience_yrs;

-- High Risk Deliveriries

SELECT
    Order_ID,
    Traffic_Level,
    Weather,
    Delivery_Time_min,
    Profit
FROM food_delivery
WHERE Delivery_Time_min > 60
AND Profit < 200
ORDER BY Delivery_Time_min DESC;

-- This mimics:
-- operational anomaly detection,
-- logistics incident reporting,
-- escalation analytics.

-- Best Operational Conditions

SELECT
    Traffic_Level,
    Weather,
    Vehicle_Type,
    ROUND(AVG(Profit_Margin), 2) AS avg_profit_margin
FROM food_delivery
GROUP BY Traffic_Level, Weather, Vehicle_Type
ORDER BY avg_profit_margin DESC
LIMIT 10;

