#!/usr/bin/node

const fs = require('fs');

const fA = fs.readFileSync(process.argv[2]);
const fB = fs.readFileSync(process.argv[3]);
fs.writeFileSync(process.argv[4], fA + fB);
