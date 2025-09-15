% macro prefix_table(environment, table_name) %}
  {{ environment }}_{{ table_name }}
{% endmacro %}


-- Example usage in a model
-- SELECT * FROM {{ ref(prefix_table('prod', 'fact_orders')) }}


# .github/workflows/dbt-ci.yml
name: dbt CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  dbt:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        environment: [dev, prod]

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dbt dependencies
        run: |
          python -m pip install --upgrade pip
          pip install dbt-core dbt-postgres dbt-utils

      - name: Configure profiles.yml
        run: |
          mkdir -p ~/.dbt
          echo "${{ secrets.PROFILES_YML }}" > ~/.dbt/profiles.yml
        shell: bash

      - name: dbt deps
        run: dbt deps

      - name: dbt seed
        run: dbt seed --target ${{ matrix.environment }} --profiles-dir ~/.dbt

      - name: dbt run
        run: dbt run --target ${{ matrix.environment }} --profiles-dir ~/.dbt

      - name: dbt test
        run: dbt test --target ${{ matrix.environment }} --profiles-dir ~/.dbt

      - name: dbt snapshot
        run: dbt snapshot --target ${{ matrix.environment }} --profiles-dir ~/.dbt

      - name: dbt docs generate
        run: dbt docs generate --target ${{ matrix.environment }} --profiles-dir ~/.dbt
