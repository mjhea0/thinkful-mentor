'use strict';

// modules
var express = require('express'),
    session = require('express-session'),
    bodyParser = require('body-parser');

// create express app
var app = express();

// middleware
app.use(session({
    secret: 'keyboard cat',
    resave: false,
    saveUninitialized: true
}))
app.use(bodyParser.urlencoded({ extended: false }))

var users = {"admin": "admin", "test": "test"};

// authentication
var authenticate = function(req, res, next) {
    console.log('authenticating...');
    if (!req.session.user) {
        res.redirect('/login');
    } else {
        next();
    }
};

// routes

app.get('/', authenticate, function(req, res) {
    res.send('Welcome, ' + req.session.user + '. <a href="/logout">Logout</a>');
});

app.get('/login', function(req, res) {
    if (req.session.user) {
        res.redirect('/');
    };
    var error = req.session.loginError ? '<em>' + req.session.loginError + '</em><br>' : '';
    var html = '<!DOCTYPE html>'+
                  '<html>'+
                    '<body>'
                      +error+
                      '<form action="/login" method="POST">' +
                        '<input type="text" name="username" placeholder="username"><br>' +
                        '<input type="password" name="password" placeholder="password"><br>' +
                        '<input type="submit" value="Login">' +
                      '</form>' +
                    '</body>' +
                  '<html>';
    res.send(html);
});

app.post('/login', function(req, res) {
    var username = req.body.username;
    var password = users[username];
    if (password && password === req.body.password) {
        req.session.loginError = null;
        req.session.user = username;
        res.redirect('/');
    } else {
        req.session.loginError = 'Wrong username or password.';
        res.redirect('/login');
    }
});

app.get('/logout', function(req, res) {
    req.session.destroy();
    res.redirect('/');
});

app.get('/hey', authenticate, function(req, res) {
    res.send('Hello, ' + req.session.user + '. This is another secured page.');
});

app.listen(3000);
console.log('Listening on port 3000...');