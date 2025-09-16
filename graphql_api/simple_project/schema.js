const { gql } = require('apollo-server-express');

const typeDefs = gql`
  type Author {
    id: ID!
    name: String!
    books: [Book]
  }

  type Book {
    id: ID!
    title: String!
    author: Author
  }

  type Query {
    books: [Book]
    authors: [Author]
    book(id: ID!): Book
  }

  type Mutation {
    addBook(title: String!, authorId: ID!): Book
  }
`;

module.exports = typeDefs;