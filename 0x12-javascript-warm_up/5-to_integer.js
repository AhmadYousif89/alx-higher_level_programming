#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(arg) || arg === '') {
  console.log('Not a number');
  process.exit(1);
}

console.log('My number:', +arg);
