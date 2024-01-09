#!/usr/bin/node

const dict = {
  C: 'fun',
  Python: 'cool',
  JavaScript: 'amazing'
};
for (const key in dict) {
  console.log(`${key} is ${dict[key]}`);
}
