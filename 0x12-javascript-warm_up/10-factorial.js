#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);

function factorial (firstArg) {
  if ((typeof firstArg === 'number' && firstArg === 0) || isNaN(firstArg)) {
    return 1;
  } else if (typeof firstArg === 'number' && firstArg > 0) {
    return firstArg * factorial(firstArg - 1);
  }
}

console.log(factorial(firstArg));
