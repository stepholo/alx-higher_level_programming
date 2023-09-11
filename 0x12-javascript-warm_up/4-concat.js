#!/usr/bin/node
if (process.argv.length === 2) {
  const argString = 'undefined';
  console.log(`${argString} is ${argString}`);
} else if (process.argv.length > 2) {
  const arg1 = process.argv[2] || 'undefined';
  const arg2 = process.argv[3] || 'undefined';
  console.log(arg1 + ' is ' + arg2);
}
