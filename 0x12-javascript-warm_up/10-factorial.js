#!/usr/bin/node

const number = parseInt(process.argv[2]);

function factoria (number) {
  if (!number) {
    return 1;
  }
  if (number <= 1) {
    return 1;
  }
  return (number * factoria(number - 1));
}
console.log(factoria(number));
