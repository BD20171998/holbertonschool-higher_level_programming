#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);
let i;

if (typeof firstArg === 'number' && !isNaN(firstArg)) {
  for (i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
