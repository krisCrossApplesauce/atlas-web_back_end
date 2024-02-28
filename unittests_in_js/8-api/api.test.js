const app = require('./api');
const sinon = require('sinon');
const assert = require('assert');
const chai = require('chai');
const expect = chai.expect;

describe('Test app from 8-api/api.js', () => {
  let spy;

  beforeEach(() => {
    spy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    spy.restore();
  });

  it('tests status code', () => {
    expect(spy.calledWith('API available on localhost port 7865')).to.be.true;
    expect(spy.calledOnce).to.be.true;
  });

  it('tests result', () => {
    assert.equal(0, 0);
  });
});
