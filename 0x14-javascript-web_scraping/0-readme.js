#!/usr/bin/node
// script that reads and prints the content of a file.

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) =>
  err ? console.log(err) : console.log(data)
);
