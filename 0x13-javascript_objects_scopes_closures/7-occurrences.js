#!/usr/bin/node

// returns the number of occurences in a list
// https://www.w3resource.com/javascript-exercises/fundamental/javascript-fundamental-exercise-70.php

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, value) => (value === searchElement ? count + 1 : count), 0);
};
