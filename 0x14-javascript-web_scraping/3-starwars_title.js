#!/usr/bin/node
// Importing the 'request' module
const request = require('request');

// Define the API endpoint with the post ID
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

// Making a GET request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    process.exit(1);
  }

  // Parsing the JSON response
  const movieData = JSON.parse(body);
 
  // Printing the title of the movie
  console.log(movieData.title);
});
