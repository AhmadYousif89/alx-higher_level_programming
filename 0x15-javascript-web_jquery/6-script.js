// updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header

const $ = window.$;
const cta = $('#update_header');
const header = $('header');
cta.mouseover(() => cta.css('cursor', 'pointer'));
cta.click(() => {
  if (header.text() !== 'New Header!!!') header.text('New Header!!!');
});
