#!/usr/bin/node

//returns the number of occurences in a list

exports.nbOccurences = function (list, searchElement){
    return list.reduce((count, value) => (value === searchElement ? count + 1 : count), 0);
}
