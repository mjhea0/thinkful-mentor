var http = require('http');
var url = require('url');
var items = ["first", "second", "third", "fourth", "fifth"];
var key;
var item;

var server = http.createServer(function (req, res) {

    // helper functions
    var getItem = function() {
        var pathname = url.parse(req.url).pathname;
        return parseInt(pathname.slice(1),10);
    };

    var handleItemNum = function(index) {
        if (isNaN(index)) {
            res.statusCode = 400;
            res.end('Item id is not valid');
        } else if (!items[index]) {
            res.statusCode = 404;
            res.end('Item not found');
        } else {
            return true;
        }
    };

    // crud
    switch (req.method) {
        case 'POST':
            item = '';
            req.setEncoding('utf8');
            req.on('data', function (chunk) {
                item += chunk;
            });
            req.on('end', function () {
                items.push(item);
                console.log("items are " + items);
                res.end('Item added\n');
            });
            break;
        case 'GET':
            items.forEach(function(item, i) {
                res.write(i + '. ' + item + '\n');
            });
            res.end();
            break;
        case 'DELETE':
            key = getItem();
            if (handleItemNum(key)) {
                items.splice(key,1);
                res.end('Item deleted successfully');
                console.log("items is " + items);
            }
            break;
        case 'PUT':
            key = getItem();
            if (handleItemNum(key)) {
                item = '';
                req.setEncoding('utf8');
                req.on('data', function (chunk) {
                    item += chunk;
                });
                req.on('end', function () {
                    items[key] = item;
                    res.end('Item changed\n');
                    console.log("items is " + items);
                });
            }
            break;
    }
});

server.listen(9000, function(){
    console.log('listening on 9000...');
});