#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let h = 0; h < this.height; h++) {
      let row = '';
      for (let w = 0; w < this.width; w++) {
        row += c || 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Square;
