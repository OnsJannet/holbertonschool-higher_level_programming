#!/usr/bin/node
// exports a function

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
