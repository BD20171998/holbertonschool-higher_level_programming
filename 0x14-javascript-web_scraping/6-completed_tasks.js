#!/usr/bin/node
const request = require('request');
const args = process.argv;
const requestURL = args[2];
request.get(requestURL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const list = {};
    let user = 'default';
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed) {
        if (!(data[i].userId in list)) {
          user = data[i].userId;
          list[user] = 0;
        }
        list[user] += 1;
      }
    }
    console.log(list);
  }
});
