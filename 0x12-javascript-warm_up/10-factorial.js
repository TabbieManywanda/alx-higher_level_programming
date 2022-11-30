#!/usr/bin/node

const process = require('process');
const args = process.argv;
const value = Number(args[2]);

function fact (num) {
  if (num === 0 || isNaN(num) === true) {
    return 1;
  }
  return num * fact(num - 1);
}
console.log(fact(value));
