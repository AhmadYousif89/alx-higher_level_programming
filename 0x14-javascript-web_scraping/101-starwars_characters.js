#!/usr/bin/node
// script that prints all characters of a Star Wars movie in the same order as they appeared in the movie.

const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

async function printCharactersInOrder() {
  try {
    const response = await requestPromise(url);
    const characters = JSON.parse(response.body).characters;

    for (const character_url of characters) {
      const response = await requestPromise(character_url);
      console.log(JSON.parse(response.body).name);
    }
  } catch (err) {
    console.log(err);
  }
}

printCharactersInOrder();
