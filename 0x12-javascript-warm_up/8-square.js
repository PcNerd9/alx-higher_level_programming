#!/usr/bin/node

const number = Number(process.argv[2]);
let row = '';
if (number) {
  for (let i = 0; i < number; i++) {
    row = '';
    for (let j = 0; j < number; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
