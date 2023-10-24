#!/usr/bin/node

const fs = require('fs');

const request = require('request');

const requestUrl = process.argv[2];
const fileName = process.argv[3];

request(requestUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    fs.writeFile(fileName, body, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
