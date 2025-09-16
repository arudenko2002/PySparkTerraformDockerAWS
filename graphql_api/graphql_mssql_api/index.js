const express = require('express');
const { ApolloServer } = require('apollo-server-express');
const typeDefs = require('./schema');
const resolvers = require('./resolvers');
const { sequelize } = require('./models/index');
const Author = require('./models/Author');
const Book = require('./models/Book');

async function startServer() {
  const app = express();
  const server = new ApolloServer({ typeDefs, resolvers });

  await sequelize.authenticate();
  console.log('✅ Connected to MSSQL');

  await sequelize.sync({ alter: true }); // auto-create tables

  await server.start();
  server.applyMiddleware({ app });

  app.listen({ port: 4000 }, () =>
    console.log(`🚀 Server ready at http://localhost:4000${server.graphqlPath}`)
  );
}

startServer();