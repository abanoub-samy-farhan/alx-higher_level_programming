#!/usr/bin/node

const request = require('request');
const url = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];

request.get(url, function(err, resp, body){
    if (err){
        console.log(err);
    }
    else {
        const people = JSON.parse(body).characters;
        for (let i = 0; i < people.length; i++) {
            request.get(people[i], {json: true}, (err_1, resp_1, body_1) => {
                if (err_1){
                    console.log(err_1);
                } else {
                    console.log(body_1.name);
                }
            });
        }
    }
});