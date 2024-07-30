#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function(err, resp, body){
    if (err){
        console.log(err);
    }
    else {
        console.log(body.split('/people/18').length - 1);
    }
});