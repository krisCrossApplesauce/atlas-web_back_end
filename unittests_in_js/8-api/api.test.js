const server = require('./api');
const request = require('request');
const chai = require('chai');
const expect = chai.expect;

describe('Test server from 8-api/api.js', () => {
  it('tests GET / and status code', (done) => {
    request('http://localhost:7865', (err, res, bod) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('tests that GET / returns "Welcome to the payment system"', (done) => {
    request('http://localhost:7865', (err, res, bod) => {
      expect(bod).to.equal('Welcome to the payment system');
      done();
    });
  });
});

// to stop the server after the tests should have finished running
const stopServer = setTimeout(() => {
  server.close();
}, 2000)
