var http = require('http');
var mongoose = require('mongoose');
var Item = require('./items');
var root = __dirname;
var port = 9000;


var server = http.createServer(function(req, res){
  var item = new Item({name : "Blue Widget"});

  res.end(item);

}).listen(9000, function(){
  console.log('Listening on ', port);
})