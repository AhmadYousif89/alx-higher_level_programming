#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

const characterId = '18';
const filmsUrl = process.argv[2];
request(filmsUrl, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const characterUrl = JSON.parse(body).results[0].characters.find(url =>
    url.includes(characterId)
  );
  request(characterUrl, (err, res, body) =>
    err ? console.log(err) : console.log(JSON.parse(body).films.length)
  );
});
