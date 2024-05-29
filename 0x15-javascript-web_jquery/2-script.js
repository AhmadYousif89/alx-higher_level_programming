// updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header

const $ = window.$;
const cta = $('#red_header');
const header = $('header');
cta.mouseover(() => cta.css('cursor', 'pointer'));
cta.click(() => header.css('color', '#FF0000'));
