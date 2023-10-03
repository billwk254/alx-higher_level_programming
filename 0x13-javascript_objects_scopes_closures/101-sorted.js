#!/usr/bin/node

const originalDict = require('./101-data').dict;
const reversedDict = {};

Object.keys(originalDict).map((key, index) => {
  if (reversedDict[originalDict[key]] === undefined) {
    reversedDict[originalDict[key]] = [];
  }
  reversedDict[originalDict[key]].push(key);
});

console.log(reversedDict);

