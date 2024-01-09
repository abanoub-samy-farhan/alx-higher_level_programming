#!/usr/bin/node

const argument = process.argv[2];
const argInt = parseInt(argument);
let flat = 1;

function factorial (num) {
  for (let i = 1; i < argInt; i++) {
    flat = flat * i;
  }
  return flat;
}

if (isNaN(argInt)) {
  console.log(flat);
} else if (argInt > 0) {
  console.log(factorial(argInt));
}
