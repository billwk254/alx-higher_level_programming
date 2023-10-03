#!/usr/bin/node

const originalDict = require('./101-data').dict;

const reversedDict = {};

for (const [key, value] of Object.entries(originalDict)) {
  reversedDict[value] ? reversedDict[value].push(key) : (reversedDict[value] = [key]);
}

console.log(reversedDict);
