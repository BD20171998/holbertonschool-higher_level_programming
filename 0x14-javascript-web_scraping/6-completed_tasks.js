#!/usr/bin/node

const request = require('request');

const args = process.argv;
const requestURL = args[2];

request.get(requestURL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    if (data.length === undefined) {
      throw err;
    }
    const list = {};
    let user = 'default';

    for (let i = 0; i < data.length; i++) {
      if (list[i] === undefined) {
        user = data[i].userId;
        list[user] = 0;
      }
    }

    for (let j = 0; j < data.length; j++) {
      if (data[j].completed === true) {
        user = data[j].userId;
        list[user] += 1;
      }
    }

    console.log(list);
  }
});
