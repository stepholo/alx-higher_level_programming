#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  const myArray = [];
  for (const arg of args) {
    myArray.push(arg);
  }
  let largest = myArray[0];
  let secondLargest = myArray[1];
  for (const num of myArray) {
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }
  console.log(secondLargest);
}
