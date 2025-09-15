const { authors, books } = require('./data');

let bookIdCounter = books.length + 1;

const resolvers = {
  Query: {
    books: () => books,
    authors: () => authors,
    book: (_, { id }) => books.find((b) => b.id === id),
  },
  Mutation: {
    addBook: (_, { title, authorId }) => {
      const authorExists = authors.find((a) => a.id === authorId);
      if (!authorExists) throw new Error("Author not found");

      const newBook = {
        id: String(bookIdCounter++),
        title,
        authorId,
      };
      books.push(newBook);
      return newBook;
    },
  },
  Book: {
    author: (book) => authors.find((a) => a.id === book.authorId),
  },
  Author: {
    books: (author) => books.filter((b) => b.authorId === author.id),
  },
};

module.exports = resolvers;