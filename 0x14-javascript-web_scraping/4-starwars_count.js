#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const results = JSON.parse(body).results;
  const movieCount = results.reduce((count, movie) => {
    return movie.characters.find(character => character.includes('18')) ? ++count : count;
  }, 0);
  console.log(movieCount);
});
