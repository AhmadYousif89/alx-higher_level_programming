// fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
// and displays it in the HTML tag DIV#character

const $ = window.$;
const character = $('#character');
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, data => character.text(data.name));
