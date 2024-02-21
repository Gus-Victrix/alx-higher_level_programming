#!/usr/bin/node

const request = require('request');
const ep = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/';

request(URL + ep, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
