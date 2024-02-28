const promise = Promise.resolve({data: 'Successful response from the API'});

async function getPaymentTokenFromAPI(success) {
  if (success === true) {
    return await promise;
  }
}

module.exports = getPaymentTokenFromAPI;
