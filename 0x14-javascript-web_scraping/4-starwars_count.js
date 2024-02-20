#!/usr/bin/node

const axios = require('axios');
const URL = process.argv[2];

async function getMethod (URL) {
  await axios.get(`${URL}`)
    .then((res) => {
      let counter = 0;
      for (const film of res.data.results) {
        for (const listActors of film.characters) {
          if (listActors.includes('people/18/')) {
            counter++;
          }
        }
      }
      console.log(counter);
    })
    .catch((err) => {
      console.error(err);
    });
}

getMethod(URL);
