#!/usr/bin/node

const request = require('request');
const url = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];

request.get(url, function(err, resp, body){
    if (err){
        console.log(err);
    }
    else{
        const people = JSON.parse(body).characters;
        for (const person of people){
            request.get(person, function(err, resp, body){
                if (err){
                    console.log(err);
                }
                else {
                    console.log(JSON.parse(body).name);
                }
            });
        }
    }
});