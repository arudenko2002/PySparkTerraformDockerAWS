-- models/staging/stg_customers.sql

SELECT
    id AS customer_id,
    first_name,
    last_name,
    email,
    created_at
FROM {{ source('raw', 'customers') }}