#!/usr/bin/node

// prints 3 phrases.

const count = process.argv[2];
if (parseInt(count)) {
  console.log('C is fun \n'.repeat(count));
} else {
  console.log('Missing number of occurrences');
}
