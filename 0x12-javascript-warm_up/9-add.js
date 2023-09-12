#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
if (!isNaN(a) && typeof a === 'number' && !isNaN(b) && typeof b === 'number') {
  function add (a, b) {
    const c = a + b;
    console.log(`${c}`);
  }
  add(a, b);
} else {
  console.log('Nan');
}
