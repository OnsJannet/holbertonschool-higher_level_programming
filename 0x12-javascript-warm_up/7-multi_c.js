#!/usr/bin/node

// prints 3 phrases.

const count = process.argv[2];
const string = 'C is fun';
if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (let repeat = 0; repeat < count; repeat++) {
    console.log(string);
  }
}
