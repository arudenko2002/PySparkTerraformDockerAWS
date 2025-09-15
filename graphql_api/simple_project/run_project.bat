mkdir graphql-library-api
cd graphql-library-api
npm init -y

@REM Install required packages:
npm install express apollo-server-express graphql

@REM graphql-library-api/
@REM ├── index.js          # Server setup
@REM ├── schema.js         # GraphQL type definitions
@REM ├── resolvers.js      # Logic to fetch and mutate data
@REM ├── data.js           # Sample in-memory data
@REM └── package.json

node ./init.js