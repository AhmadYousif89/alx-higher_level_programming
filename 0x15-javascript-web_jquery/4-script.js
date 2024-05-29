// toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header

const $ = window.$;
const cta = $('#toggle_header');
const header = $('header');
cta.mouseover(() => cta.css('cursor', 'pointer'));
cta.click(() => {
  if (header.hasClass('green')) header.removeClass('green').addClass('red');
  else header.addClass('green').removeClass('red');
});
