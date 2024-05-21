#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const characters = JSON.parse(body).characters;
  characters.forEach(characterUrl =>
    request(characterUrl, (err, res, body) =>
      err ? console.log(err) : console.log(JSON.parse(body).name)
    )
  );
});
