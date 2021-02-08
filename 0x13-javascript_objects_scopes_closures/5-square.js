#!/usr/bin/node

// a class square that inherits from Rectangle
class Square extends require('./4-rectangle') {
  constructor (length) {
    super(length, length);
  }
}
module.exports = Square;
