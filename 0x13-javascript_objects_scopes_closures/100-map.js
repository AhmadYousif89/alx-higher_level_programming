#!/usr/bin/node
// for our case it should be "./tests/100-data.js"
const list = require('./100-data.js').list;

console.log(list);
console.log(list.map((e, i) => e * i));
