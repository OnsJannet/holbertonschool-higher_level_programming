#!/usr/bin/node

// a class square that inherits from Rectangle
class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let count = 0; count < this.width; count++) {
        console.log('C'.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
