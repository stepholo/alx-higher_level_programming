#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];

const requestURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(requestURL, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const datas = JSON.parse(body);

  if (datas.hasOwnProperty('characters')) {
    datas.characters.forEach(characterURL => {
	    request(characterURL, (error, response, body) => {
        if (error) {
		    console.error(error);
        }

        const names = JSON.parse(body);

        console.log(names.name);
	    });
    });
  }
});
