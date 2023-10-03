#!/usr/bin/node

const originalDict = require('./101-data').dict;
const reversedDict = {};

for (const userId in originalDict) {
  const occurrence = originalDict[userId];

  if (!reversedDict[occurrence]) {
    reversedDict[occurrence] = [];
  }

  reversedDict[occurrence].push(userId);
}

console.log(reversedDict);
