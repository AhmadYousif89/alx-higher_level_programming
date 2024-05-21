#!/usr/bin/node
// script that display the status code of a GET request.

const request = require('request');

request(process.argv[2], (err, res) =>
  err ? console.log(err) : console.log('code:', res.statusCode)
);
