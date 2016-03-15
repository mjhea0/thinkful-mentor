var chai = require('chai');
var chaiHttp = require('chai-http');
var server = require('../server.js');

var should = chai.should();
var app = server.app;
var storage = server.storage;

chai.use(chaiHttp);

describe('Shopping List', function() {
  it('should list items on GET', function(done) {
    chai.request(app)
      .get('/items')
      .end(function(err, res) {
        res.should.have.status(200);
        res.should.be.json; // jshint ignore:line
        res.body.should.be.a('array');
        res.body.should.have.length(3);
        res.body[0].should.be.a('object');
        res.body[0].should.have.property('id');
        res.body[0].should.have.property('name');
        res.body[0].id.should.be.a('number');
        res.body[0].name.should.be.a('string');
        res.body[0].name.should.equal('Broad beans');
        res.body[1].name.should.equal('Tomatoes');
        res.body[2].name.should.equal('Peppers');
        done();
      });
  });

  it('should add an item on POST', function(done) {
    chai.request(app)
      .post('/items')
      .send({'name': 'Kale'})
      .end(function(err, res) {
        should.equal(err, null);
        res.should.have.status(201);
        res.should.be.json; // jshint ignore:line
        res.body.should.be.a('object');
        res.body.should.have.property('name');
        res.body.should.have.property('id');
        res.body.name.should.be.a('string');
        res.body.id.should.be.a('number');
        res.body.name.should.equal('Kale');
        storage.items.should.be.a('array');
        storage.items.should.have.length(4);
        storage.items[3].should.be.a('object');
        storage.items[3].should.have.property('id');
        storage.items[3].should.have.property('name');
        storage.items[3].id.should.be.a('number');
        storage.items[3].name.should.be.a('string');
        storage.items[3].name.should.equal('Kale');
        done();
      });
  });

  it('should edit an item on put', function(done) {
    chai.request(app)
      .put('/items/1')
      .send({'name': 'Milk', id: "1"})
      .end(function(err, res) {
        should.equal(err, null);
        res.should.have.status(201);
        res.should.be.json; // jshint ignore:line
        res.body.should.be.a('object');
        res.body.should.have.property('name');
        res.body.should.have.property('id');
        res.body.name.should.be.a('string');
        res.body.id.should.be.a('number');
        res.body.name.should.equal('Milk');
        storage.items.should.be.a('array');
        storage.items.should.have.length(4);
        storage.items[1].should.be.a('object');
        storage.items[1].should.have.property('id');
        storage.items[1].should.have.property('name');
        storage.items[1].id.should.be.a('number');
        storage.items[1].name.should.be.a('string');
        storage.items[1].name.should.equal('Milk');
        done();
      });
  });

  it('should delete an item on delete', function(done) {
    chai.request(app)
      .delete('/items/2')
      .end(function(err, res) {
        should.equal(err, null);
        res.should.have.status(201);
        res.should.be.json; // jshint ignore:line
        res.body.should.be.a('object');
        res.body.should.have.property('name');
        res.body.should.have.property('id');
        res.body.name.should.be.a('string');
        res.body.id.should.be.a('number');
        res.body.name.should.equal('Peppers');
        storage.items.should.be.a('array');
        storage.items.should.have.length(3);
        storage.items[0].name.should.equal('Broad beans');
        storage.items[1].name.should.equal('Milk');
        storage.items[2].name.should.equal('Kale');
        done();
      });
  });

  it('should return error for delete request that does not exist', function(done) {
    chai.request(app)
      .delete('/items/5')
      .end(function(err, res) {
        err.should.have.status(400);
        res.should.be.json; // jshint ignore:line
        res.body.should.be.a('object');
        res.body.should.have.property('error');
        res.body.error.should.equal('no item found');
        storage.items.should.be.a('array');
        storage.items.should.have.length(3);
        storage.items[0].name.should.equal('Broad beans');
        storage.items[1].name.should.equal('Milk');
        storage.items[2].name.should.equal('Kale');
        done();
      });
  });

});
