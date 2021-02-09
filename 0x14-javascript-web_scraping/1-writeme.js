#!/usr/bin/node

// write a string to a file.

/* File System Object */
const fs = require('fs');
/* Read File, write on a file */
fs.writeFile(process.argv[2], process.argv[3], 'utf8',
  function (error) {
  /* If an error exists, show it */
    if (error) console.log(error);
  });
