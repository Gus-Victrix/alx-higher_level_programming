#!/usr/bin/node

const args = process.argv.slice(2);
let largest = 0;
let secondLargest = 0;

args.forEach((element) => {
  element = parseInt(element);
  if (element > largest) {
    secondLargest = largest;
    largest = element;
  } else if (element > secondLargest) {
    secondLargest = element;
  }
});
console.log(secondLargest);
