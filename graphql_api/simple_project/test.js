// test.js
const { graphql, buildSchema } = require('graphql');

// 1. Define a simple GraphQL schema
const schema = buildSchema(`
  type Query {
    hello: String
  }
`);

// 2. Provide resolver functions for the schema
const root = {
  hello: () => {
    return 'Hello world!';
  },
};

// 3. Execute a test query
graphql({
  schema,
  source: '{ hello }',
  rootValue: root,
}).then((response) => {
  console.log(JSON.stringify(response, null, 2));
});
