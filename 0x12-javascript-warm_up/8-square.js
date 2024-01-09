#!/usr/bin/node

const argument = process.argv[2];
const argInt = parseInt(argument);

if (isNaN(argInt)) {
  console.log('Missing size');
} else if (argInt > 0) {
  console.log(('X'.repeat(argInt) + '\n').repeat(argInt - 1) + 'X'.repeat(argInt));
}
