// script that fetches and prints how to say “Hello” depending on the language

const $ = window.$;
const url = 'https://hellosalut.stefanbohacek.dev/';
$(function () {
  $('#btn_translate').after('<small id="lang-ex">Ex : ar, fr, en</small>');
  $('#lang-ex').css({ display: 'block', color: '#555' });
  $('#btn_translate').click(() => {
    $('#hello').empty();
    const lang = $('#language_code').val();
    $.get(`${url}?lang=${lang}`, data => $('#hello').append(data.hello));
  });
  $('#language_code').keypress(function (e) {
    if (e.which == 13) {
      $('#btn_translate').click();
      return false;
    }
  });
});
