var sqlite3 = require('sqlite3').verbose();

var dbFile;
switch(process.env.NODE_ENV.toUpperCase()) {
  case 'PROD': dbFile = 'production.sqlite3';   break;
  case 'TEST': dbFile = 'test.sqlite3';         break;
  default:     dbFile = 'development.sqlite3';  break;
}

var file = 'db/' + dbFile;
var db = new sqlite3.Database(file);
db.file = file;
module.exports = db;
