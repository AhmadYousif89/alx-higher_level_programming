// adds a <li> element to a list when the user clicks on the tag DIV#add_item

const $ = window.$;
const cta = $('#add_item');
const list = $('.my_list');
cta.mouseover(() => cta.css('cursor', 'pointer'));
cta.click(() => list.append('<li>Item</li>'));
