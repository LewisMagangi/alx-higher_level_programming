#!/usr/bin/node
function factorial (a) {
  let result = 1;
  for (let i = 2; i <= a; i++) {
    result *= i;
  }
  console.log(result);
}

// Call the factorial function with the first command line argument
factorial(process.argv[2]);
