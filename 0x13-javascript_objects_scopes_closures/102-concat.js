#!/usr/bin/node

const fs = require('fs');

const rf1 = process.argv[2];
const rf2 = process.argv[3];
const wf = process.argv[4];

if (!rf1 || !rf2 || !wf) {
  process.exit(1);
}

const rf1Data = fs.readFileSync(rf1);
const file2Data = fs.readFileSync(rf2);
fs.writeFileSync(wf, `${rf1Data}\n${file2Data}`);

