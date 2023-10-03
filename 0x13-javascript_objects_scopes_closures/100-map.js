#!/usr/bin/node

const data = require('./100-data');
const list = data.list;

console.log(list);
const newList = list.map((value, index) => value * index);
console.log(newList);
