const { DataTypes } = require('sequelize');
const { sequelize } = require('./index');
const Author = require('./Author');

const Book = sequelize.define('Book', {
  title: {
    type: DataTypes.STRING,
    allowNull: false,
  },
});

Book.belongsTo(Author, { foreignKey: 'authorId', as: 'author' });
Author.hasMany(Book, { foreignKey: 'authorId', as: 'books' });

module.exports = Book;