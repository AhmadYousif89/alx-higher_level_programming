// script that adds, removes and clears LI elements from a list

const $ = window.$;
$(() => {
  const ul = $('UL.my_list');
  const add = $('DIV#add_item');
  const remove = $('DIV#remove_item');
  const clear = $('DIV#clear_list');
  const hoverInHandler = function (color = '#FF0000') {
    $(this).css({ cursor: 'pointer', width: 'fit-content', color });
  };
  const hoverOutHandler = function () {
    $(this).css({ cursor: 'pointer', width: 'fit-content', color: '' });
  };
  add.hover(function () {
    hoverInHandler.call(this, 'green');
  }, hoverOutHandler);
  remove.hover(function () {
    hoverInHandler.call(this, 'coral');
  }, hoverOutHandler);
  clear.hover(function () {
    hoverInHandler.call(this, '#FF0000');
  }, hoverOutHandler);

  const el = '<li>Item</li>';
  let i = 0;

  add.click(() => ul.append(el.replace('Item', 'Item ' + i++)));
  remove.click(() => {
    ul.children().last().remove();
    i--;
  });
  clear.click(() => {
    ul.empty();
    i = 0;
  });
});
