#!/usr/bin/node

const imp = require('fs');
const argv = process.argv;

const file1 = imp.readFileSync(argv[2], 'utf-8').toString();
const file2 = imp.readFileSync(argv[3], 'utf-8').toString();
imp.writeFileSync(argv[4], file1 + file2);
