#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    const fetchCharacterName = (characterUrl, characterIndex) => {
      request(characterUrl, (characterError, characterResponse, characterBody) => {
        if (!characterError && characterResponse.statusCode === 200) {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        } else {
          console.error(`Error fetching character data: ${characterError}`);
        }

        // Check if this is the last character to print
        if (characterIndex === characters.length - 1) {
          process.exit(0);
        }
      });
    };

    characters.forEach((characterUrl, characterIndex) => {
      fetchCharacterName(characterUrl, characterIndex);
    });
  } else {
    console.error(`Request failed with status code: ${response.statusCode}`);
  }
});
