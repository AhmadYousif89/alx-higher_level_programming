#!/usr/bin/node

function getFactorial(n) {
	if (isNaN(n) || n === 1) return 1;
	return n * getFactorial(n - 1);
}

console.log(getFactorial(process.argv[2]));
