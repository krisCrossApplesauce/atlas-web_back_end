const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');
const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;

describe("Test sendPaymentRequestToApi function from 3-payment.js", () => {
  it('calling sendPaymentRequestToApi should call calculateNumber method from Utils module', () => {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('SUM', 100, 20)).to.be.true;

    spy.restore();
  }); 
});
