SELECT
    id AS order_id,
    customer_id,
    order_date,
    status,
    total_amount,
    updated_at
FROM {{ source('raw', 'orders') }}