{{ config(materialized='table') }}
SELECT
    c.customer_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    email,
    status,
    total_amount,
    order_date,
    created_at
FROM {{ ref('stg_customers') }} as c
JOIN {{ ref('stg_orders') }} as o
on c.customer_id=o.customer_id