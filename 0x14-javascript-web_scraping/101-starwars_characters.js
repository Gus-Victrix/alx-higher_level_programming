#!/usr/bin/node

const axios = require('axios');

const id = process.argv[2];
const URL = `https://swapi-api.hbtn.io/api/films/${id}`;

async function getMethod (URL) {
  await axios.get(URL)
    .then(async (res) => {
      for (const characters of res.data.characters) {
        await axios.get(characters)
          .then((res) => {
            console.log(res.data.name);
          });
      }
    }).catch((err) => {
      console.log(`code: ${err.response.status}`);
    });
}

getMethod(URL);
