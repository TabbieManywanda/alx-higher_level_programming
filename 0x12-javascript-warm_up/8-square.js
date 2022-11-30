#!/usr/bin/node

const process = require('process');
const args = process.argv;
const num = parseInt(args[2]);
const row = 'X'.repeat(num);

if (isNaN(num) === true) {
  console.log('Missing size');
}

let i = 0;
while (i < num) {
  console.log(row);
  i++;
}
