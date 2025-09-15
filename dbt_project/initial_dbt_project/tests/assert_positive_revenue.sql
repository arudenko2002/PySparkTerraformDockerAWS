SELECT *
FROM {{ ref('dim_customers') }}
WHERE len(full_name) = 0