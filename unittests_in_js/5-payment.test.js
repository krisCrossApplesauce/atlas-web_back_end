const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');
const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;

describe("Test sendPaymentRequestToApi function from 5-payment.js", () => {
  let spy;

  beforeEach(() => {
    spy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    spy.restore();
  });

  it('calls sendPaymentRequestToApi with 100 and 20', () => {
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledWith('The total is: 120')).to.be.true;
    expect(spy.calledOnce).to.be.true;
  });

  it('calls sendPaymentRequestToApi with 10 and 10', () => {
    sendPaymentRequestToApi(10, 10);
    expect(spy.calledWith('The total is: 20')).to.be.true;
    expect(spy.calledOnce).to.be.true;
  }); 
});
