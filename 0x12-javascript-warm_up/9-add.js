#!/usr/bin/node
function add (a, b) {
  console.log(Number(a) + Number(b));
}
// Get command line arguments
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Call the add function with command line arguments
add(arg1, arg2);
