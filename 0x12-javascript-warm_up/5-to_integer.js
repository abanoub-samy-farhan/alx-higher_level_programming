#!/usr/bin/node

const argument = process.argv[2];

const intArg = parseInt(argument);

if (!isNaN(intArg)) {
  console.log(`My number: ${intArg}`);
} else {
  console.log('Not a number');
}
