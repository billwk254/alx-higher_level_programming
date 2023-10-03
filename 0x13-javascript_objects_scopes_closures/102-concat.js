#!/usr/bin/node

const fs = require('fs');
const filePath1 = process.argv[2];
const filePath2 = process.argv[3];
const destinationPath = process.argv[4];

try {
  const data1 = fs.readFileSync(filePath1, 'utf8');
  const data2 = fs.readFileSync(filePath2, 'utf8');

  const concatenatedData = data1 + data2;

  fs.writeFileSync(destinationPath, concatenatedData);
}

