#!/usr/bin/node
const convertInt = parseInt(process.argv[2]);
if (!isNaN(convertInt) && typeof convertInt === 'number') {
  console.log(`My number: ${convertInt}`);
} else {
  console.log('Not a number');
}
