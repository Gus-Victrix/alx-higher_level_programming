#!/usr/bin/node

const axios = require('axios');
const fs = require('fs');

const URL = process.argv[2];
const pathFile = process.argv[3];

async function resquestLoremAPI (URL, pathFile) {
  await axios.get(URL)
    .then((res) => {
      if (res.status === 200) {
        fs.writeFile(`./${pathFile}`, res.data, { flag: 'w+' }, err => {
          if (err) {
            console.error(err);
          }
        });
      }
    })
    .catch((err) => {
      console.error(err);
    });
}

resquestLoremAPI(URL, pathFile);
