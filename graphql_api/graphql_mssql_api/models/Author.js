const { DataTypes } = require('sequelize');
const { sequelize } = require('./index');

const Author = sequelize.define('Author', {
  name: {
    type: DataTypes.STRING,
    allowNull: false,
  },
});

module.exports = Author;