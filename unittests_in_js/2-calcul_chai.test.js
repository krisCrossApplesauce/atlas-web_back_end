const calculateNumber = require('./2-calcul_chai');
const chai = require('chai');
const expect = chai.expect;

describe("Test calculateNumber function from 2-calcul_chai.js", () => {
// SUM
  it("adds two numbers", () => {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
  });

  it("rounds and adds two numbers", () => {
	  expect(calculateNumber('SUM', 1.7, 3)).to.equal(5);
  });

  it("rounds and adds two numbers", () => {
	  expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
  });

  it("rounds and adds two numbers", () => {
	  expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
  });

  it("rounds and adds two numbers", () => {
	  expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
  });

  it("rounds and adds two numbers", () => {
	  expect(calculateNumber('SUM', 1.7, 3.2)).to.equal(5);
  });

  it("rounds and adds two numbers", () => {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });

// SUBTRACT
	it("subtracts two numbers", () => {
    expect(calculateNumber('SUBTRACT', 1, 4)).to.equal(-3);
	});

	it("rounds and subtracts two numbers", () => {
    expect(calculateNumber('SUBTRACT', 1.7, 4)).to.equal(-2);
	});

	it("rounds and subtracts two numbers", () => {
    expect(calculateNumber('SUBTRACT', 1, 4.5)).to.equal(-4);
	});

	it("rounds and subtracts two numbers", () => {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
	});

	it("rounds and subtracts two numbers", () => {
    expect(calculateNumber('SUBTRACT', 5.7, 4.2)).to.equal(2);
	});

// DIVIDE
	it("returns the string 'Error' bc you can't divide by 0", () => {
    expect(calculateNumber('DIVIDE', 1, 0)).to.equal('Error');
	});

	it("returns the string 'Error' bc you can't divide by 0", () => {
    expect(calculateNumber('DIVIDE', 1, -0.1)).to.equal('Error');
	});

	it("divides two numbers", () => {
    expect(calculateNumber('DIVIDE', 4, 2)).to.equal(2);
	});

	it("rounds and divides two numbers", () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
	});

	it("rounds and divides two numbers", () => {
    expect(calculateNumber('DIVIDE', 4.5, 1.4)).to.equal(5);
	});

	it("divides two numbers", () => {
    expect(calculateNumber('DIVIDE', 0, 1)).to.equal(0);
	});
});
