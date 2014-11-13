var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var inventory = require('./inventory');

var app = express();
var expressHbs = require('express-handlebars');

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.engine('hbs',expressHbs({extname:'hbs',defaultLayout:'main.hbs'}));
app.set('view engine', 'hbs');

// uncomment after placing your favicon in /public
//app.use(favicon(__dirname + '/public/favicon.ico'));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.route('/')
    .get(inventory.list)
    .post(inventory.create);
app.get('/new', inventory.new);
app.route('/:id').get(inventory.show).post(inventory.update).delete(inventory.delete);
app.route('/:id/edit').get(inventory.edit);

/*
app.get('/', inventory.list);
app.post('/', inventory.create);
app.get('/new', inventory.new);
app.get('/:id', inventory.show);
app.post('/:id', inventory.update);
app.delete('/id', inventory.delete);
app.get('/:id/edit', inventory.edit);
*/


// catch 404 and forward to error handler
app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

// error handlers

// development error handler
// will print stacktrace
if (app.get('env') === 'development') {
    app.use(function(err, req, res, next) {
        res.status(err.status || 500);
        res.render('error', {
            message: err.message,
            error: err
        });
    });
}

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res, next) {
    res.status(err.status || 500);
    res.render('error', {
        message: err.message,
        error: {}
    });
});


module.exports = app;
