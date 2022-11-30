#!/usr/bin/node

const process = require('process');
const args = process.argv;
const list = [];

if (args.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    list.push(Number(args[i]));
  }
  list.sort(function (a, b) { return b - a; });
  console.log(list[1]);
}
