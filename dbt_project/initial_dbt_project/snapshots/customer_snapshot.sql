{% snapshot customer_snapshot %}
{{
  config(
    target_schema='snapshots',
    unique_key='customer_id',
    strategy='check',
    check_cols=['email', 'full_name', 'status']
  )
}}

SELECT
    id AS customer_id,
    email,
    CONCAT(first_name, ' ', last_name) AS full_name,
    status,
    created_at,
    updated_at
FROM {{ source('raw', 'customers') }}
WHERE updated_at >= DATEADD(month, -6, GETDATE())

{% endsnapshot %}