{{ config(
    materialized='incremental',
    unique_key='order_id',
    on_schema_change='sync_all_columns'
) }}

SELECT
    o.id AS order_id,
    o.customer_id,
    o.order_date,
    o.status,
    o.total_amount
FROM {{ source('raw', 'orders') }}  o
WHERE o.order_date >= '2023-01-01'

{% if is_incremental() %}
  -- Only new or updated orders
  AND o.updated_at > (SELECT MAX(updated_at) FROM {{ this }})
{% endif %}