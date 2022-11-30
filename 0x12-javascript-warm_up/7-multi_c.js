#!/usr/bin/node

const process = require('process');
const args = process.argv;
const num = parseInt(args[2]);

if (isNaN(num) === true) {
  console.log('Missing number of occurences');
}

let i = 0;
while (i < num) {
  console.log('C is fun');
  i++;
}
