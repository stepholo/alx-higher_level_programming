#!/usr/bin/node
const request = require('request')

const requestURL = process.argv[2];
const characterurl = `https://swapi-api.alx-tools.com/api/people/18/`;

request.get(requestURL, (error, response, body) => {
	if (error) {
		console.error(err);
		return;
	}

	const data = JSON.parse(body).results;

	const moviesWithWedge = data.filter(datas =>
		datas.characters.includes(characterurl));
	
	console.log(`${moviesWithWedge.length}`);
});
