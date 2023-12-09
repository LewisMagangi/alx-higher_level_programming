#!/usr/bin/node
class Rectangle {
  // This is a class Rectangle that defines a rectangle:
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // If w or h is equal to 0 or not a positive integer, create an empty object
      const emptyRectangle = new Rectangle();
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
