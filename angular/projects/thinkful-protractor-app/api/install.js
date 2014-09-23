var fs = require('fs');
var colors = require('colors');

var db = require('./db');

if (fs.existsSync(db.file)) {
  console.log(("\n   The database file \"" + db.file + "\" already exists... Please remove it if you wish to re-install\n").yellow);
  return;
}

db.serialize(function() {
  db.run("CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT, shortened_url TEXT, title TEXT)");
  console.log('Created the `urls` table');
});
