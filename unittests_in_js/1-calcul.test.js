const calculateNumber = require('./1-calcul');
const assert = require('assert');

describe("Test calculateNumber function from 1-calcul.js", () => {
// SUM
  it("adds two numbers", () => {
    assert.equal(calculateNumber('SUM', 1, 3), 4);
  });

  it("rounds and adds two numbers", () => {
    assert.equal(calculateNumber('SUM', 1.7, 3), 5);
  });

  it("rounds and adds two numbers", () => {
    assert.equal(calculateNumber('SUM', 1, 3.7), 5);
  });

  it("rounds and adds two numbers", () => {
    assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
  });

  it("rounds and adds two numbers", () => {
    assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);
  });

  it("rounds and adds two numbers", () => {
    assert.equal(calculateNumber('SUM', 1.7, 3.2), 5);
  });

	it("rounds and adds two numbers", () => {
    assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
  });

// SUBTRACT
	it("subtracts two numbers", () => {
		assert.equal(calculateNumber('SUBTRACT', 1, 4), -3);
	});

	it("rounds and subtracts two numbers", () => {
		assert.equal(calculateNumber('SUBTRACT', 1.7, 4), -2);
	});

	it("rounds and subtracts two numbers", () => {
		assert.equal(calculateNumber('SUBTRACT', 1, 4.5), -4);
	});

	it("rounds and subtracts two numbers", () => {
		assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
	});

	it("rounds and subtracts two numbers", () => {
		assert.equal(calculateNumber('SUBTRACT', 5.7, 4.2), 2);
	});

// DIVIDE
	it("returns the string 'Error' bc you can't divide by 0", () => {
		assert.equal(calculateNumber('DIVIDE', 1, 0), 'Error');
	});

	it("returns the string 'Error' bc you can't divide by 0", () => {
		assert.equal(calculateNumber('DIVIDE', 1, -0.1), 'Error');
	});

	it("divides two numbers", () => {
		assert.equal(calculateNumber('DIVIDE', 4, 2), 2);
	});

	it("rounds and divides two numbers", () => {
		assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
	});

	it("rounds and divides two numbers", () => {
		assert.equal(calculateNumber('DIVIDE', 4.5, 1.4), 5);
	});

	it("divides two numbers", () => {
		assert.equal(calculateNumber('DIVIDE', 0, 1), 0);
	});
});
