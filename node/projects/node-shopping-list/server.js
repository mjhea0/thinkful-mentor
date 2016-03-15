var express = require('express');
var jsonParser = require('body-parser').json();

var Storage = require('./models');
var storage = new Storage();
storage.add('Broad beans');
storage.add('Tomatoes');
storage.add('Peppers');

var app = express();
app.use(express.static('public'));

app.get('/items', function(req, res) {
  res.json(storage.items);
});

app.post('/items', jsonParser, function(req, res) {
  if (!req.body) {
    return res.sendStatus(400);
  }
  var item = storage.add(req.body.name);
  res.status(201).json(item);
});

app.put('/items/:id', jsonParser, function(req, res) {
  if (!req.body) {
    return res.sendStatus(400);
  }
  var item = storage.put(req.params.id, req.body.name);
  res.status(201).json(item);
});

app.delete('/items/:id', function(req, res) {
  var item = storage.remove(req.params.id);
  if (item) {
    res.status(201).json(item);
  } else {
    res.status(400).json({"error": "no item found"});
  }
});

app.listen(process.env.PORT || 8080);

exports.app = app;
exports.storage = storage;
