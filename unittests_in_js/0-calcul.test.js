const calculateNumber = require('./0-calcul');
const assert = require('assert');

describe("Test calculateNumber function from 0-calcul.js", () => {
  it("adds two numbers", () => {
    assert.equal(calculateNumber(1, 3), 4);
  });

  it("rounds and adds two numbers", () => {
    assert.equal(calculateNumber(1.7, 3), 5);
  });

  it("rounds and adds two numbers", () => {
    assert.equal(calculateNumber(1, 3.7), 5);
  });

  it("rounds and adds two numbers", () => {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  });

  it("rounds and adds two numbers", () => {
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });

  it("rounds and adds two numbers", () => {
    assert.equal(calculateNumber(1.7, 3.2), 5);
  });
});
