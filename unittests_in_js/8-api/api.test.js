const app = require('./api');
const sinon = require('sinon');
const chaiHttp = require('chai-http');
const chai = require('chai');
const expect = chai.expect;
chai.use(chaiHttp);

describe('Test app from 8-api/api.js', () => {
  it.skip('tests console.log (when server is started?)', (done) => {
    const logSpy = sinon.spy(console, 'log');
    chai.request(app);
    expect(logSpy.calledWith('API available on localhost port 7865')).to.be.true;
    expect(logSpy.calledOnce).to.be.true;
    logSpy.restore();
  });

  it('tests GET / and status code', (done) => {
    chai.request(app).get('/').end((err, res) => {
      expect(res.status).to.equal(200);
      done();
    });
  });

  it.skip('tests GET / returns "Welcome to the payment system"', (done) => {
    const resSpy = sinon.spy(app, 'res');
    chai.request(app).get('/').end((err, res) => {
      expect(resSpy.calledWith('Welcome to the payment system')).to.be.true;
      expect(resSpy.calledOnce).to.be.true;
      done();
    });
    resSpy.restore();
  });
});
