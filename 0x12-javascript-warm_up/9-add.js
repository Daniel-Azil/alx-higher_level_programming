#!/usr/bin/node 
function add (num_1, num_2) {
    return num_1 + num_2;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));