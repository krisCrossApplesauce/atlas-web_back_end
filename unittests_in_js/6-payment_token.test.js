const getPaymentTokenFromAPI = require('./6-payment_token');
const assert = require('assert');

describe('Test getPaymentTokenFromAPI from 6-payment_token.js', () => {
  it('calls getPaymentTokenFromAPI with true', async () => {
    const result = await getPaymentTokenFromAPI(true);
    assert.equal(result.data, 'Successful response from the API');
  });
});
