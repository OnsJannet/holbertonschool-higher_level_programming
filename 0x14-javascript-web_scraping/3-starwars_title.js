#!/usr/bin/node

// print the title of a Star Wars movie.

const url = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');
request(url + process.argv[2], function (error, response, body) {
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(error);
  }
});
