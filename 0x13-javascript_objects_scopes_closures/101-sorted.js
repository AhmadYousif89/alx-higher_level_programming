#!/usr/bin/node

// for our case it should be "./tests/101-data.js"
const dict = require('./101-data.js').dict;

const newDict = {};

for (const [key, value] of Object.entries(dict)) {
  newDict[value] = newDict[value] ? [...newDict[value], key] : [key];
}

console.log(newDict);
