// fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.

const $ = window.$;
$(function () {
  const $ = window.$;
  const hello = $('div#hello');
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  hello.css({
    display: 'grid',
    placeItems: 'center',
    color: '#FF0000',
    border: '2px solid #FF0000',
    borderRadius: '999px',
    width: 'fit-content',
    minHeight: '80px',
    padding: '5px',
    fontSize: '18px',
    aspectRatio: '1',
    boxShadow: '1px 1px 3px 2px #00000050'
  });
  $.get(url, data => hello.text(data.hello));
});
