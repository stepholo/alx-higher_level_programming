#!/usr/bin/node
const request = require('request')

const movieId = process.argv[2];
const requestURL = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(requestURL, (error, response, body) => {
	if (error) {
		console.error(err);
		return;
	}

	const data = JSON.parse(body);
	if (data.title) {
		console.log(data.title);
	}
});
