import duckdb

def func(query, filename):
    result = duckdb.sql(query)
    print(result)
    result.to_csv(f"output/{filename}.csv")


top_10_most_selling_skus_by_quantity_sold = """
SELECT 
    SKU_NAME, 
    sum(UNIT_SOLD) as Total_unit_sold 
FROM 'resources/assignmentData.csv' 
GROUP BY SKU_NAME 
ORDER BY Total_unit_sold DESC 
LIMIT 10
"""
func(top_10_most_selling_skus_by_quantity_sold, "top_10_most_selling_skus_by_quantity_sold")


top_10_most_selling_skus_by_value_sold = """
SELECT 
    SKU_NAME, 
    sum(TOTAL_VALUE_SOLD) as Total_value_sold 
FROM 'resources/assignmentData.csv' 
GROUP BY SKU_NAME 
ORDER BY Total_value_sold DESC 
LIMIT 10
"""
func(top_10_most_selling_skus_by_value_sold, "top_10_most_selling_skus_by_value_sold")


top_10_least_selling_skus_by_quantity_sold = """
SELECT SKU_NAME, sum(UNIT_SOLD) as Total_unit_sold 
FROM 'resources/assignmentData.csv' 
GROUP BY SKU_NAME 
ORDER BY Total_unit_sold ASC 
LIMIT 10
"""
func(top_10_least_selling_skus_by_quantity_sold, "top_10_least_selling_skus_by_quantity_sold")


top_10_least_selling_skus_By_value_sold = """
SELECT SKU_NAME, sum(TOTAL_VALUE_SOLD) as Total_value_sold 
FROM 'resources/assignmentData.csv' 
GROUP BY SKU_NAME 
ORDER BY Total_value_sold ASC 
LIMIT 10
"""
func(top_10_least_selling_skus_By_value_sold, "top_10_least_selling_skus_By_value_sold")


top_10_customers_by_total_value_purchased = """
SELECT CUSTOMER_ID, SUM(TOTAL_VALUE_SOLD) AS total_value_purchased 
FROM 'resources/assignmentData.csv' 
GROUP BY CUSTOMER_ID 
ORDER BY total_value_purchased DESC 
LIMIT 10
"""
func(top_10_customers_by_total_value_purchased, "top_10_customers_by_total_value_purchased")


top_10_sales_representatives_by_value_sold = """
SELECT SALES_REP_ID, SUM(TOTAL_VALUE_SOLD) AS total_value_sold
FROM 'resources/assignmentData.csv'
GROUP BY SALES_REP_ID
ORDER BY total_value_sold DESC
LIMIT 10
"""
func(top_10_sales_representatives_by_value_sold, "top_10_sales_representatives_by_value_sold")


top_10_sales_representatives_by_time_spent = """
SELECT 
  SALES_REP_ID, 
  SUM(EXTRACT(EPOCH FROM (strptime(CHECKOUT_TIME, '%m/%d/%Y %H:%M') - strptime(CHECKIN_TIME, '%m/%d/%Y %H:%M')))) AS total_time_spent
FROM 'resources/assignmentData.csv'
WHERE SALES_REP_ID IS NOT NULL
GROUP BY SALES_REP_ID
ORDER BY total_time_spent DESC
LIMIT 10
"""
func(top_10_sales_representatives_by_time_spent, "top_10_sales_representatives_by_time_spent")


top_10_sales_representatives_by_value_day_wise_average_value_sold = """
WITH top_sales_reps AS (
    -- First identify top 10 sales reps by total value
    SELECT 
        SALES_REP_ID,
        SALES_REP,
        SUM(TOTAL_VALUE_SOLD) as total_value
    FROM 'resources/assignmentData.csv'
    WHERE TOTAL_VALUE_SOLD IS NOT NULL
    GROUP BY SALES_REP_ID, SALES_REP
    ORDER BY SUM(TOTAL_VALUE_SOLD) DESC
    FETCH FIRST 10 ROWS ONLY
),
daily_sales AS (
    -- Calculate daily sales for top 10 reps
    SELECT 
        a.SALES_REP_ID,
        a.SALES_REP,
        CAST(strptime(a.CHECKIN_TIME, '%m/%d/%Y %H:%M') AS DATE) as sale_date,
        SUM(a.TOTAL_VALUE_SOLD) as daily_value
    FROM 'resources/assignmentData.csv' a
    INNER JOIN top_sales_reps t ON a.SALES_REP_ID = t.SALES_REP_ID
    WHERE a.TOTAL_VALUE_SOLD IS NOT NULL
    GROUP BY a.SALES_REP_ID, a.SALES_REP, CAST(strptime(a.CHECKIN_TIME, '%m/%d/%Y %H:%M') AS DATE)
)
SELECT 
    SALES_REP_ID,
    SALES_REP,
    ROUND(AVG(daily_value), 2) as avg_daily_value_sold,
    COUNT(DISTINCT sale_date) as total_days_worked,
    MIN(daily_value) as min_daily_value,
    MAX(daily_value) as max_daily_value
FROM daily_sales
GROUP BY SALES_REP_ID, SALES_REP
ORDER BY avg_daily_value_sold DESC
"""
func(top_10_sales_representatives_by_value_day_wise_average_value_sold, "top_10_sales_representatives_by_value_day_wise_average_value_sold")


top_10_sales_representatives_by_value_day_wise_average_time_spent = """
WITH top_sales_reps AS (
    SELECT 
        SALES_REP_ID,
        SALES_REP,
        SUM(TOTAL_VALUE_SOLD) as total_value
    FROM 'resources/assignmentData.csv'
    WHERE TOTAL_VALUE_SOLD IS NOT NULL
    GROUP BY SALES_REP_ID, SALES_REP
    ORDER BY SUM(TOTAL_VALUE_SOLD) DESC
    FETCH FIRST 10 ROWS ONLY
),
daily_time_spent AS (
    SELECT 
        a.SALES_REP_ID,
        a.SALES_REP,
        CAST(strptime(a.CHECKIN_TIME, '%m/%d/%Y %H:%M') AS DATE) as work_date,
        SUM(
            (CAST(strptime(a.CHECKOUT_TIME, '%m/%d/%Y %H:%M') AS DATE) - 
            CAST(strptime(a.CHECKIN_TIME, '%m/%d/%Y %H:%M') AS DATE))*24*60
        ) as daily_minutes
    FROM 'resources/assignmentData.csv' a
    INNER JOIN top_sales_reps t ON a.SALES_REP_ID = t.SALES_REP_ID
    WHERE a.CHECKIN_TIME IS NOT NULL 
      AND a.CHECKOUT_TIME IS NOT NULL
    GROUP BY a.SALES_REP_ID, a.SALES_REP, CAST(strptime(a.CHECKIN_TIME, '%m/%d/%Y %H:%M') AS DATE)
)
SELECT 
    SALES_REP_ID,
    SALES_REP,
    ROUND(AVG(daily_minutes), 2) as avg_daily_minutes,
    ROUND(AVG(daily_minutes)/60, 2) as avg_daily_hours,
    COUNT(DISTINCT work_date) as total_days_worked,
    ROUND(MIN(daily_minutes), 2) as min_daily_minutes,
    ROUND(MAX(daily_minutes), 2) as max_daily_minutes
FROM daily_time_spent
GROUP BY SALES_REP_ID, SALES_REP
ORDER BY avg_daily_minutes DESC;
"""
func(top_10_sales_representatives_by_value_day_wise_average_time_spent, "top_10_sales_representatives_by_value_day_wise_average_time_spent")