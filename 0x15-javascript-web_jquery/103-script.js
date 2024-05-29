// script that fetches and prints how to say “Hello” depending on the language

const $ = window.$;
const url = 'https://www.fourtonfish.com/hellosalut/hello/';
$(function () {
  $('#btn_translate').click(() => {
    const lang = $('#language_code').val();
    $.get(`${url}?lang=${lang}`, data => $('#hello').text(data.hello));
  });
  $('#language_code').keypress(function (e) {
    if (e.which == 13) {
      $('#btn_translate').click();
      return false;
    }
  });
});
