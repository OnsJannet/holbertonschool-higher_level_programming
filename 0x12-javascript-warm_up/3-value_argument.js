#!/usr/bin/node

// prints a message depending of the number of arguments passed:

const string = process.argv[2];
if (string === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
