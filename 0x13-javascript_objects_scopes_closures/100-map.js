#!/usr/bin/node
const { list } = require('./100-data');
console.log(list);
const multipliedList = list.map((element, index) => {
  return element * index;
});
console.log(multipliedList);
