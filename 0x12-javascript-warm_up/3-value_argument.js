#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  process.argv.slice(2).forEach((arg, index) => {
    console.log(arg);
  });
}
