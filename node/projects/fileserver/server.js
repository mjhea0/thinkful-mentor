// include the built-in modules http and fs ("file system")
var http = require('http');
var fs = require('fs');

// create a nodejs server using the http module
http.createServer(function (req, res) {

    fs.readFile('data.txt', function readData(err, data) {
        // set the status code of the HTTP response to 200 which indicates success
        // set the Content-Type to text/plain
      res.writeHead(200, {'Content-Type': 'text/plain'});

      // output the data in the response
      res.end(data);
    })

}).listen(9000, '127.0.0.1');

console.log('Server running at http://127.0.0.1:9000/');