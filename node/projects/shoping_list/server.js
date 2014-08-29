var http = require('http');
var url = require('url');
var items = ["first", "second", "third", "fourth", "fifth"];
var idx;
var item;

var server = http.createServer(function (req, res) {

    var getItemNumFromUrl = function() {
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

    switch (req.method) {
        case 'POST':
            item = '';
            req.setEncoding('utf8');
            req.on('data', function (chunk) {
                item += chunk;
            });
            req.on('end', function () {
                items.push(item);
                console.log("items is " + items);
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
            idx = getItemNumFromUrl();
            if (handleItemNum(idx)) {
                items.splice(idx,1);
                res.end('Item deleted successfully');
                console.log("items is " + items);
            }
            break;
        case 'PUT':
            idx = getItemNumFromUrl();
            if (handleItemNum(idx)) {
                item = '';
                req.setEncoding('utf8');
                req.on('data', function (chunk) {
                    item += chunk;
                });
                req.on('end', function () {
                    items[idx] = item;
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