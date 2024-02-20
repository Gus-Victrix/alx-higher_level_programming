#!/usr/bin/node

const axios = require('axios');
const ep = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films';

async function getMethod (URL, ep) {
  await axios.get(`${URL}/${ep}`)
    .then((res) => {
      console.log(`${res.data.title}`);
    })
    .catch((err) => {
      console.error(`code :${err.response.status}`);
    });
}

getMethod(URL, ep);
