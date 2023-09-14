#!/usr/bin/node
const fs = require('fs');

const firstFile = String(process.argv[2]);
const secondFile = String(process.argv[3]);
const thirdFile = String(process.argv[4]);

let dOne, dTwo;
fs.readFile(firstFile, 'utf8', (err, dataOne) => {
  if (err) {
    console.error(err);
    return;
  }
  dOne = String(dataOne);
  fs.readFile(secondFile, 'utf8', (err, dataTwo) => {
    if (err) {
      console.error(err);
      return;
    }
    dTwo = String(dataTwo);
    fs.writeFile(thirdFile, dOne, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
    fs.appendFile(thirdFile, dTwo, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});
