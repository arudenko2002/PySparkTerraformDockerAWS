{% macro prefix_table(environment, table_name) %}
  {{ environment }}_{{ table_name }}
{% endmacro %}

--usage:
--SELECT * FROM {{ ref(prefix_table('prod', 'fact_orders')) }}