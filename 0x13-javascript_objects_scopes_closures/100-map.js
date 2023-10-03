#!/usr/bin/node

const list = require('./100-data').list;
const newList = list.map((data, value) => data * value);
console.log(list);
console.log(newList);
