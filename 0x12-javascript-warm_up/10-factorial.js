#!/usr/bin/node

const argument = process.argv[2];
const argInt = parseInt(argument);
let flat = 1;

if (isNaN(argInt)) {
  console.log(flat);
} else if (argInt > 0) {
  for (let i = 1; i < argInt; i++) {
    flat = flat * i;
  }
  console.log(flat);
}
