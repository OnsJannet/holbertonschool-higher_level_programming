#!/usr/bin/node

// get the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
request(process.argv[2], function (error, response, body) {
  if (response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf-8', function (error) {
      if (error) console.log(error);
    }
    );
  } else {
    console.log(error);
  }
});
