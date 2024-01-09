#!/usr/bin/node

const arguments = process.argv.slice(2).map(Number); // Convert arguments to numbers

if (arguments.length === 0) {
  console.log(0);
} else if (arguments.length === 1) {
  console.log(0);
} else {
  const uniqueList = [...new Set(arguments)];
  const sortedList = uniqueList.sort((a, b) => b - a);
  console.log(sortedList[1]);
}