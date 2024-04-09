#!/usr/bin/node

const fs = require('fs');

const f1 = process.argv[2];
const f2 = process.argv[3];
const out = process.argv[4];

const f1Data = fs.readFileSync(f1, 'utf-8');
const f2Data = fs.readFileSync(f2, 'utf-8');
fs.writeFileSync(out, `${f1Data}\n${f2Data}\n`);
