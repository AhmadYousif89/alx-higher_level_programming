#!/usr/bin/node

const args = process.argv.slice(2);
const argsLen = args.length;

if (argsLen < 2) {
	console.log(0);
	return;
}

let max = +args[0];
let secondMax = -Infinity;

for (let i = 0; i < args.length; i++) {
	let num = +args[i];
	if (num > max) {
		secondMax = max;
		max = num;
	} else if (num > secondMax && num < max) {
		secondMax = num;
	}
}

console.log(secondMax);
