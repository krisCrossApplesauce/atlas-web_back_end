const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;

describe("Test sendPaymentRequestToApi function from 4-payment.js", () => {
  it('calling sendPaymentRequestToApi should call calculateNumber method from Utils module', () => {
    const stub = sinon.stub(Utils, 'calculateNumber');
    const spy = sinon.spy(console, 'log');

    stub.returns(10);

    sendPaymentRequestToApi(100, 20);

    expect(stub.calledWith('SUM', 100, 20)).to.be.true;
    expect(spy.calledWith('The total is: 10')).to.be.true;

    stub.restore();
    spy.restore();
  }); 
});
