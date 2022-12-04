#!/usr/bin/node

const list1 = require('./100-data');
const newList = list1.map((element, index) => element * index);
console.log(list1);
console.log(newList);
