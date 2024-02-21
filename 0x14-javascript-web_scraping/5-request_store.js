#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const pathFile = process.argv[3];

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(pathFile, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
