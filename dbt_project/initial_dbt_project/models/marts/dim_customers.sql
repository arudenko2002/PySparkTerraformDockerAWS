-- models/marts/dim_customers.sql
{{ config(materialized='view') }}
SELECT
    customer_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    email,
    created_at
FROM {{ ref('stg_customers') }}