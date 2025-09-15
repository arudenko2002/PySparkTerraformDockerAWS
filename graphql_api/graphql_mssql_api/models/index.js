const { Sequelize } = require('sequelize');
require('dotenv').config();
// ✅ Create Sequelize instance with proper MSSQL config
const sequelize = new Sequelize(
  process.env.DB_NAME,       // database name
  process.env.DB_USER,       // username
  process.env.DB_PASSWORD,   // password
  {
    host: process.env.DB_HOST,     // or 'localhost'
    dialect: process.env.DB_DIALECT,
    port: process.env.DB_PORT, // default MSSQL port
    logging: false,
    dialectOptions: {
      options: {
        encrypt: false,               // set true if you're using Azure
        trustServerCertificate: true, // for local dev
        //server: process.env.DB_HOST,
      }
    }
  }
);

module.exports = { sequelize };