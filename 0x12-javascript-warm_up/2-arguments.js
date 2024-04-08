#!/usr/bin/node

const argsLen = process.argv.length;
const phrase = argsLen > 2 ? `Argument${argsLen > 3 ? 's' : ''} found` : 'No argument';
console.log(phrase);
