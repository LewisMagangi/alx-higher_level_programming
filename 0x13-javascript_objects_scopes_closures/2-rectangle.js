#!/usr/bin/node
class Rectangle {
  // This is a class Rectangle that defines a rectangle:
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      const emptyObject = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
