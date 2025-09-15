{% macro format_email(email) %}
    LOWER(TRIM({{ email }}))
{% endmacro %}