#!/usr/bin/node

const arg = process.argv[2];

if (arg === '' || isNaN(arg)) {
	console.log('Missing number of occurrences');
	return;
}

for (let i = 0; i < +arg; i++) {
	console.log('C is fun');
}
