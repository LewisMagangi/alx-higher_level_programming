#!/usr/bin/node

class Rectangle {
  // This is a class Rectangle that defines a rectangle:
  constructor (w, h) {
    // Check if w and h are positive integers
    if (w > 0 && h > 0) {
      // If valid, assign values to width and height
      this.width = w;
      this.height = h;
    } else {
      // If not valid, create an empty object
      this.width = 0;
      this.height = 0;
    }
  }

  // Method to print a rectangle
  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let l = 0; l < this.width; l++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
// Specify width and height for the rectangle
const w = 0;
const h = 0;

// Create an instance of Rectangle
const myRectangle = new Rectangle(w, h);

// Calling the instance method to print the rectangle
myRectangle.print();

// Export the Rectangle class
module.exports = Rectangle;
