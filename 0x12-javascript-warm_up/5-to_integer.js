#!/usr/bin/node

const arg = process.argv[2];

if (arg === '' || isNaN(arg)) {
	console.log('Not a number');
	return;
}

console.log('My number:', +arg);
