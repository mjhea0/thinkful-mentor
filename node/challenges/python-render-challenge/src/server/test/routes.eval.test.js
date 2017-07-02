process.env.NODE_ENV = 'test';

const chai = require('chai');
const chaiHttp = require('chai-http');

const server = require('../app');

chai.should();
chai.use(chaiHttp);

describe('eval api routes', () => {

  describe('GET /api/v1/eval/ping', () => {
    it('should return pong', (done) => {
      chai.request(server)
        .get('/api/v1/eval/ping')
        .end((err, res) => {
        res.type.should.equal('application/json');
        res.body.status.should.equal('success');
        res.body.data.should.eql('pong!');
        done();
      });
    });
  });

});
