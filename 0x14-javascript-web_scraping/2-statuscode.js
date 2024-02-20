#!/usr/bin/node

const axios = require('axios');

const URL = process.argv[2];

async function getMethod (URL) {
  await axios.get(URL)
    .then((res) => {
      console.log(`code: ${res.status}`);
    }).catch((err) => {
      console.log(`code: ${err.response.status}`);
    });
}

getMethod(URL);
