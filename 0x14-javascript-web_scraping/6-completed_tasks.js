#!/usr/bin/node

// compute the number of tasks completed by user id.

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completed = {};
    for (const todo in todos) {
      const task = todos[todo];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log(error);
  }
});
