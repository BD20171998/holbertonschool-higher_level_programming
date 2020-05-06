#!/usr/bin/node

const argNo = process.argv.length - 2;

if (argNo < 2) {
  console.log(0);
} else {
  const list = process.argv.slice(2);
  const list2 = list.sort(function (a, b) { return b - a; });
  console.log(list2[1]);
}
