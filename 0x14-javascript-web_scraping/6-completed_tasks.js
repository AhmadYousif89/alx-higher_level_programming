#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const tasks = JSON.parse(body);
  const completed_tasks = tasks
    .filter(task => task.completed)
    .reduce((completed, task) => {
      completed[task.userId] = (completed[task.userId] || 0) + 1;
      return completed;
    }, {});
  console.log(completed_tasks);
});
