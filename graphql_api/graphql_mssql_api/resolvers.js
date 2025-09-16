const Author = require('./models/Author');
const Book = require('./models/Book');

const resolvers = {
  Query: {
    books: async () => await Book.findAll({ include: 'author' }),
    authors: async () => await Author.findAll(),
    book: async (_, { id }) => await Book.findByPk(id, { include: 'author' }),
  },

  Mutation: {
    addAuthor: async (_, { name }) => await Author.create({ name }),
    addBook: async (_, { title, authorId }) => {
      const author = await Author.findByPk(authorId);
      if (!author) throw new Error('Author not found');
      return await Book.create({ title, authorId });
    },
  },

  Author: {
    books: async (author) => await author.getBooks(),
  },

  Book: {
    author: async (book) => await book.getAuthor(),
  },
};

module.exports = resolvers;