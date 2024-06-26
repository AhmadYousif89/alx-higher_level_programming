#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');

const episode = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episode}`;
request(url, (err, res, body) =>
  err ? console.log(err) : console.log(JSON.parse(body).title)
);
