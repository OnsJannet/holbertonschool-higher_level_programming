#!/usr/bin/node

// factorial

const interger = parseInt(process.argv[2]);
function factorial (interger) {
  if (interger === 1 || isNaN(interger)) {
    return 1;
  } else {
    return (interger * factorial(interger - 1));
  }
}
console.log(factorial(interger));
