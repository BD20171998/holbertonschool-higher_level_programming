#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);
let i;
let text = '';

if (typeof firstArg === 'number' && !isNaN(firstArg)) {
  for (i = 0; i < firstArg; i++) {
    text += 'X';
  }
  for (i = 0; i < firstArg; i++) {
    console.log(text);
  }
} else {
  console.log('Missing size');
}
