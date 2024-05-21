#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

const character_id = '18';
const films_url = process.argv[2];
request(films_url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const character_url = JSON.parse(body).results[0].characters.find(url =>
    url.includes(character_id)
  );
  request(character_url, (err, res, body) =>
    err ? console.log(err) : console.log(JSON.parse(body).films.length)
  );
});
