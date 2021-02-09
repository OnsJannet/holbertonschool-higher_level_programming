#!/usr/bin/node

// display the status code of a GET request.

const request = require('request');
request(process.argv[2], function (error, response) {
  console.log(error || 'code: ' + response.statusCode);
});
