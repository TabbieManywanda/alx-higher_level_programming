#!/usr/bin/node

const process = require('process');
const args = process.argv;
const num = parseInt(args[2]);

if (isNaN(num) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
