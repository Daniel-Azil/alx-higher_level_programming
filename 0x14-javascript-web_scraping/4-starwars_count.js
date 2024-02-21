#!/usr/bin/node

let url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let film_list = JSON.parse(body).results;
    let count = 0;
    for (let i in film_list) {
      let encounter = film_list[i].characters;
      for (let c in encounter) {
	if (encounter[c].includes('18')) {
	  count++;
	}
      }
    }
    console.log(count);
  } else {
    console.log('Could not Process:' + response.statusCode);
  }
});