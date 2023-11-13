#!/usr/bin/node

const occ = parseInt(process.argv[2]);
if (isNaN(occ)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < occ; i++) {
    console.log('C is fun');
  }
}
