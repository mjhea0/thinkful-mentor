var http = require("http");
var auth = require("http-auth");

var basic = auth.basic({file: __dirname + '/auth'});
console.log(basic.options)

http.createServer(basic, function(req, res) {
    res.end('User authenticated: ' + req.user);
}).listen(9000, '127.0.0.1');


console.log('Server running at http://127.0.0.1:9000/');