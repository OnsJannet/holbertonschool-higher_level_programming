#!/usr/bin/node

/* print the number of movies where the character
 “Wedge Antilles” is present. */

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (response.statusCode === 200) {
    let count = 0;
    const list = JSON.parse(body).results;
    for (const people in list) {
      const characters = list[people].characters;
      for (const character in characters) {
        if (characters[character].endsWith('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
