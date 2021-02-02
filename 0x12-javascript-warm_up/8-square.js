#!/usr/bin/node

// prints a square

const count = process.argv[2];
const character = 'x';
if (isNaN(count)) {
  console.log('Missing size');
} else {
  for (let repeat = 0; repeat < count; repeat++) {
    console.log(character.repeat(count));
  }
}
