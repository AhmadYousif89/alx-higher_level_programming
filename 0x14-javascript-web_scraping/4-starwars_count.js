#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

const filmsUrl = process.argv[2];
request(filmsUrl, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const characterUrl = JSON.parse(body).results[0].characters.find(url =>
    url.includes(18 || '18')
  );
  request(characterUrl, (err, res, body) =>
    err ? console.log(err) : console.log(JSON.parse(body).films.length)
  );
});
