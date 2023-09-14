#!/usr/bin/node
let noalreadyPrint = 0;
exports.logMe = function (item) {
  console.log(`${noalreadyPrint++}: ${item}`);
};
