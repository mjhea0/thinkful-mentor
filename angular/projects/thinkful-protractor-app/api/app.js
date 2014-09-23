var express = require('express');

var ctrl = require('./ctrl.js');

var api = express(); 
api.get('/urls',            ctrl.index);
api.get('/urls/:urlId',     ctrl.show);
api.post('/urls',           ctrl.create);
api.put('/urls/:urlId',     ctrl.update);
api.delete('/urls/:urlId',  ctrl.remove);
api.get('/g/:uid',          ctrl.jump);

api.param('urlId', ctrl.instance);
api.param('uid', ctrl.instanceByUrl);
module.exports = api;
