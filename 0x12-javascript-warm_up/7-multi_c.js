#!/usr/bin/node
const convertInt = parseInt(process.argv[2]);
if (!isNaN(convertInt) && typeof convertInt === 'number') {
  for (let i = 0; i < convertInt; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
