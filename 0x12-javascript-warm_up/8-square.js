#!/usr/bin/node
const x = process.argv[2];
const y = typeof x;
if (((y === 'number' || y === 'string') && !isNaN(x))) {
  for (let i = 0; i < parseInt(x); i++) {
    let row = '';
    for (let l = 0; l < parseInt(x); l++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
