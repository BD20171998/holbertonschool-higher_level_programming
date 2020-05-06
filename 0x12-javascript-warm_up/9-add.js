#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);
const secArg = parseInt(process.argv[3]);

function add () {
  if (typeof firstArg === 'number' && !isNaN(firstArg) && typeof secArg ===
      'number' && !isNaN(secArg)) {
    return firstArg + secArg;
  } else {
    return NaN;
  }
}
console.log(add());
