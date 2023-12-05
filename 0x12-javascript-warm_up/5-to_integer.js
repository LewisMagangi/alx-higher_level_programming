#!/usr/bin/node
if (typeof(process.agrv[2]) === 'number' || typeof(process.agrv[2]) === 'string')
{
  console.log('My number: ' + parseInt(process.agrv[2]) || 'Not a number')
} else 
{
  console.log('Not a number')
}
