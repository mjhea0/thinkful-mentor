var db = require('./db.js');
var md5 = require('md5');
var prefix = "/g/";

module.exports = {
  
  index : function(req, res) {
    db.serialize(function() {
      db.all("SELECT * FROM urls", function(err, rows) {
        res.json(rows);
      });
    });
  },

  create : function(req, res) {
    var url = req.body.url;
    var title = req.body.title;

    db.serialize(function() {
      db.get("SELECT * FROM urls ORDER BY id DESC LIMIT 1", function(err, row) {
        var nextID = (row ? parseInt(row.id) : 0) + 1;
        var snip = md5(Math.random() + '-' + Date.now()).substring(0, 10);
        var shortened_url = prefix + nextID + snip;

        var sql = "INSERT INTO urls (url, shortened_url, title) VALUES (" +
                    "'" + url + "', " +
                    "'" + shortened_url + "', " +
                    "'" + title + "'" +
                  ")";
          
        db.run(sql, function(err) {
          res.json({
            id : nextID,
            ok : !err
          });
        });
      });
    });
  },

  update : function(req, res) {
    var title = req.body.title;
    var id = req.id;

    db.serialize(function() {
      db.run("UPDATE urls SET title='" + title + "' WHERE id='" + id + "'", function(err) {
        console.log(err);
        res.json({
          ok : !err
        });
      });
    });
  },

  show : function(req, res) {
    res.json(req.url);
  },

  remove : function(req, res) {
    var id = req.id;
    db.run("DELETE FROM urls WHERE id='" + id + "'", function(err) {
      res.json({
        ok : !err
      });
    });
  },

  instance : function(req, res, next, id) {
    db.get("SELECT * FROM urls WHERE id='" + id + "' LIMIT 1", function(err, row) {
      req.id = id;
      req.url = row;
      next();
    });
  },

  instanceByUrl : function(req, res, next, id) {
    db.get("SELECT * FROM urls WHERE shortened_url='" + prefix + id + "' LIMIT 1", function(err, row) {
      req.id = id;
      req.url = row;
      next();
    });
  },

  jump : function(req, res) {
    console.log(req.url);
    res.redirect(req.url.url);
  }

};
