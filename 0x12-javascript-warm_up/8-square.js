#!/usr/bin/node

const number = parseInt(process.argv[2]);
let value;

if (!number) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    value = '';
    for (let i = 0; i < number; i++) {
      value += 'X';
    }
    console.log(value);
  }
}
