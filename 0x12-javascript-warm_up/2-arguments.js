#!/usr/bin/node
const { argv } = require('node:process');

// printing the argv if found

if (process.argv.length <= 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}