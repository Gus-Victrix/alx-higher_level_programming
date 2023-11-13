#!/usr/bin/node

const result = parseInt(process.argv[2]);
if (isNaN(result)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + result);
}
