var http = require('http');
var server = http.createServer(function(req, res){
	res.write('Hello World');
	res.end();

});
server.listen(9000, function(){
	console.log('listening on port 9000');
});