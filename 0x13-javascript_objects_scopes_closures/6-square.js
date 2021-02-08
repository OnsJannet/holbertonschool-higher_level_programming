#!/usr/bin/node

// a class square that inherits from Rectangle
class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let count = 0; count < this.height; count++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
