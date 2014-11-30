'use strict';

// modules
var express = require('express'),
    auth = require('basic-auth');

// create express app
var app = express();


// authentication
function authenticate (user, password) {
    return user === "admin" && password == "secret";
}

function basic (req, res, next) {
    var user = auth(req);
    if (user !== undefined && authenticate(user.name, user.pass)) {
        return next();
    } else {
        res.status(401).set({
            'WWW-Authenticate': 'Basic realm="localhost"'
        }).send();
    }
}

// routes

app.get('/newAuth', basic, function (req, res) {
    res.send("you made it past basic-auth");
});

app.get('/login', function (req, res) {
    console.log("arrived A");
});

app.get('/', authenticate, function(req, res) {
    res.send("hello, " + req.session.user + '.');
    console.log('arrived B');
});

app.listen(8080, function(){
    console.log('listening on port ' + 8080);
});