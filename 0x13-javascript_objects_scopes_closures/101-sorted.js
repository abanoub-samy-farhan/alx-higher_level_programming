#!/usr/bin/node
const dict = require('./data_sorted').dict;
const obj = {};
for (const key in dict) {
  if (typeof (obj[dict[key]]) === 'undefined') {
    obj[dict[key]] = [];
  }
  obj[dict[key]].push(key);
}
console.log(obj);
