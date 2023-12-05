#!/usr/bin/node
if (typeof ((process.argv[2]) === 'number' || typeof (process.argv[2]) === 'string') && !isNaN(process.argv[2])) {
  console.log('My number: ' + parseInt(process.argv[2]) || 'Not a number');
} else {
  console.log('Not a number');
}
