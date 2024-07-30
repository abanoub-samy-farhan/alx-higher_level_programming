#!/usr/bin/node

const fileToWrite = process.argv[2];
const content = process.argv[3];
const fs = require('fs');

fs.writeFile(fileToWrite, content, ({encoding:'utf-8'}), function (err, data){
    if (err){
        console.log(err);
    }
});