#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function(err, resp, body){
    if (err){
        console.log(err);
    }
    else{
        const completeTasks = {};
        const tasks = JSON.parse(body);
        for (const task of tasks){
            if (task.completed == true)
            {
                completeTasks[task.userId] = (completeTasks[task.userId] | 0) + 1;
            }
        }
        console.log(completeTasks);
    }
});