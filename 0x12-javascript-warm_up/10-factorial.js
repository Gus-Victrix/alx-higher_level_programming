#!/usr/bin/node
const myVar = process.argv[2];

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(parseInt(myVar)));
