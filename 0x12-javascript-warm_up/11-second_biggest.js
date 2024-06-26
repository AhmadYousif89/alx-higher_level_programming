#!/usr/bin/node

const args = process.argv.slice(2);
const argsLen = args.length;

if (argsLen < 2) {
  console.log(0);
  process.exit(1);
}

let max = +args[0];
let secondMax = -Infinity;

for (let i = 0; i < args.length; i++) {
  const num = +args[i];
  if (num > max) {
    secondMax = max;
    max = num;
  } else if (num > secondMax && num < max) {
    secondMax = num;
  }
}

console.log(secondMax);
