#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  fs.writeFile(filePath, body, 'utf8', () => {});
});
