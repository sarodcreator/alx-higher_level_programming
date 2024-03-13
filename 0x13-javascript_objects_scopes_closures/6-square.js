#!/usr/bin/node
// A class Square that defines a square and inherits from Rectangle

const Rectangle = require('./5-square');
class Square extends Rectangle {
  charPrint (c) {
    let newchar = '';
    if (c === undefined) {
      newchar = 'X';
    } else {
      newchar = c;
    }
    let i = 0;
    for (i = 0; i < this.height; i++) {
      let row = 0;
      let col = '';
      for (row = 0; row < this.width; row++) {
        col += newchar;
      }
      console.log(col);
    }
  }
}
module.exports = Square;

