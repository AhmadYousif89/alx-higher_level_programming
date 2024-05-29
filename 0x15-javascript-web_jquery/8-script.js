// fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
// The title of the movies should be listed in the HTML tag UL#list_movies

const $ = window.$;
$(function () {
  const $ = window.$;
  const list = $('#list_movies');
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, data => {
    for (const movie of data.results) {
      list.append($(`<li>${movie.title}</li>`));
    }
  });
});
