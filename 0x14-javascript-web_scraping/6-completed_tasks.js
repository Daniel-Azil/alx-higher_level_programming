#!/usr/bin/node

let url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let dictionary = {};
    let info = JSON.parse(body);
    for (let i in info) {
      if (info[i].completed) {
	if (dictionary[info[i].userId] === undefined) {
	  dictionary[info[i].userId] = 1;
	} else {
	  dictionary[info[i].userId]++;
	}
      }
    }
    console.log(dictionary);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});