#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18; // ID for Wedge Antilles

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const filmsData = JSON.parse(body);
      const filmsWithWedgeAntilles = filmsData.results.filter(film =>
        film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
      );
      console.log(filmsWithWedgeAntilles.length);
    } else {
      console.error(`Request failed with status code: ${response.statusCode}`);
    }
  }
});
