#!/usr/bin/node
// Import the Rectangle class
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Pass size as both width and height to the Rectangle constructor

    // Check if size is a positive integer
    if (size > 0) {
      // If valid, assign value to size
      this.size = size;
    } else {
      // If not valid, create an empty
      this.size = 0;
    }
  }
}

// Export the Square class
module.exports = Square;
