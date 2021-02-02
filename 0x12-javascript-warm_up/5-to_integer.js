#!/usr/bin/node

// prints a message depending of the number of arguments passed:

const number = process.argv[2];
if (parseInt(number)) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
