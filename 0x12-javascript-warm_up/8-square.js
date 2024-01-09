#!/usr/bin/node

const argument = process.argv[2];
const argInt = parseInt(argument);

if (isNaN(argInt)) {
  console.log('Missing size');
} else if (argInt > 0) {
  for (let i = 0; i < argInt; i++) {
    console.log('X'.repeat(argInt));
  }
}
