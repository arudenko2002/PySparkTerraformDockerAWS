dbt seed          # Load static CSVs
dbt run           # Run models (incremental logic kicks in)
dbt snapshot      # Run snapshots
dbt test          # Run built-in and custom tests
dbt docs generate # Generate documentation
dbt docs serve    # Serve interactive docs