// adds the class red to the <header> element when the user clicks on the tag DIV#red_header

const $ = window.$;
const cta = $('#red_header');
const header = $('header');
cta.mouseover(() => cta.css('cursor', 'pointer'));
cta.click(() => header.addClass('red'));
