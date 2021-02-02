#!/usr/bin/node

// prints 3 phrases.

const variable = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (const phrase in variable) {
  console.log(variable[phrase]);
}
