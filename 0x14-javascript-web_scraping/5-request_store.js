#!/usr/bin/node

const request = require('request');
const filename = process.argv[3];
const fs = require('fs');
const url = process.argv[2];

request.get(url, function(err, resp, body){
    if (err){
        console.log(err);
    }
}).pipe(fs.createWriteStream(filename, ({encoding:'utf-8'})));