#!/usr/bin/node

let id_of_movie = process.argv[2];
let url = 'http://swapi.co/api/films/' + id_of_movie;
const request = require('request')

request(url, function(err, response, body) {
    if (err) {
        console.log(err);
    } else if (response.statusCode === 200) {
        body = JSON.parse(body);
        console.log(body['title']);
    } else {
        console.log('Could not Process:' + response.statusCode);
    }
});