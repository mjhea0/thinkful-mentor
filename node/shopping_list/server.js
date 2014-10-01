// requirements
var http = require('http'),
    url = require('url'),
    qs = require('querystring');

// globals
var items = ["apples", "chicken", "bananas", "corn", "kale"];
var itemsList = "";
var idx;

// styles
var bootstrapStyles = "<head><link href='http://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css' rel='stylesheet' media='screen'>"
var customStyles = "<style>.container {max-width: 400px; padding-top: 20px;}</style></head>"

// html for POST form
var postForm = "<body><div class='container'><h1>Shopping List!</h1><br><form action='/' role='form' method='post'>"+
               "<input type='text' name='item' class='form-control' placeholder='Enter an item...' required><br>"+
               "<button type='submit' class='btn btn-default'>Add</button><br><br>";

var editFormPre = "<body><div class='container'><form action='/' role='form' method='post'><input type='hidden' name='index' value='";
var editFormPost = "'><input type='text' name='item' class='form-control' placeholder='Edit the item...' required><br>"+
                   "<button type='submit' class='btn btn-default'>Edit</button></div></body>";

var getItems = function (req,res) {
  itemsList = bootstrapStyles+customStyles+postForm+"<body><ul>";
  items.forEach(function(item, i) {
    itemsList += "<li id='"+i+"'><a href='/"+i+"'>"+item+"</a> - <a href='/"+i+"/delete'>X</a></li>";
  });
  itemsList += "</ul><br><p>(click an item to edit, or the x to delete)</div></body>";
  res.writeHead(200,{"Content-Type": "text/html"});
  res.write(itemsList);
  res.end();
};

var server = http.createServer(function (req, res) {

  var pathname = url.parse(req.url).pathname;

  var getItemNumFromUrl = function() {
    var pathname = url.parse(req.url).pathname;
    return parseInt(pathname.slice(1),10);
  };

  var handleItemNum = function(index) {
    if (isNaN(index)) {
      res.statusCode = 400;
      res.end('That item is not valid!');   // test by entering a string in the url
    } else if (!items[index]) {
      res.statusCode = 404;
      res.end('Item not found! Try again.');  // test by entering an invalid item number in the url
    } else {
      return true;
    }
  };

    switch (req.method) {
      case 'POST':
        formData = '';
        req.setEncoding('utf8');
        req.on('data', function (chunk) {
          formData += chunk;
        });
        req.on('end', function () {
          var formObj = qs.parse(formData);
          var idx = parseInt(formObj.index,10);
          var item = formObj.item;
          if(idx){
            items[idx] = item;
          } else {
            items.push(item);
          }
          getItems(req,res);
          res.end('Item added!\n');
        });
        break;
      case 'GET':
        if(pathname.indexOf('delete')!== -1 ){
          idx = getItemNumFromUrl();
          if (handleItemNum(idx)) {
            items.splice(idx,1);
            getItems(req,res);
            res.end('Item deleted!');
            break;
        }
        } else if(typeof parseInt(pathname.slice(1),10) === "number" && !isNaN(parseInt(pathname.slice(1),10))) {
          idx = getItemNumFromUrl();
          res.writeHead(200,{"Content-Type": "text/html"});
          res.write(bootstrapStyles+customStyles+editFormPre+idx+editFormPost);
          res.end();
          break;
        } else {
          getItems(req, res);
          break;
        }
    }

});

server.listen(9000, function(){
  console.log('listening on 9000...');
});