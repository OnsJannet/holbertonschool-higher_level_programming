#!/usr/bin/node

// prints a message depending of the number of arguments passed:
// if no argument passed prints no argument
// if arguments passed prints argument found.

const string = process.argv.length;
if (string === 2) {
  console.log('No argument');
} else if (string === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

// ref : https://riptutorial.com/node-js/example/10945/process-argv-command-line-arguments
