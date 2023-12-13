#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
<<<<<<< HEAD
    super(size, size); // Pass size as both width and height to the Rectangle constructor
    this.size = size;

    // Check if size is a positive integer
    if (size > 0) {
  
=======
    super(size, size);
  }
>>>>>>> 79bc7df1fd0c656105df00761d732d2e34deb5c6
}

module.exports = Square;
