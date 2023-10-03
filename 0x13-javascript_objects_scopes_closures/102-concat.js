#!/usr/bin/node

const fs = require('fs');

const argv = process.argv;

const case1 = fs.readFileSync(argv[2], 'utf-8').toString();

const case2 = fs.readFileSync(argv[3], 'utf-8').toString();
fs.writeFileSync(argv[4], case1 + case2);
