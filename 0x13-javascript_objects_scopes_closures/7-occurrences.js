#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numOfOccur = 0;
  for (const num of list) {
    if (num === searchElement) {
      numOfOccur += 1;
    }
  }
  return numOfOccur;
};
