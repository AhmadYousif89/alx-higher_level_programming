#!/usr/bin/node

const arg = process.argv[2];

if (arg === '' || isNaN(arg)) {
  console.log('Missing number of occurrences');
  process.exit(1);
}

for (let i = 0; i < +arg; i++) {
  console.log('C is fun');
}
