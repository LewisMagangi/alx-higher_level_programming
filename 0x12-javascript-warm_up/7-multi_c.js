#!/usr/bin/node
const x = process.argv[2];
const y = typeof (x);
if (((y === 'number' || y === 'string') && !isNaN(x))) {
  for (let i = 0; i < parseInt(x); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
