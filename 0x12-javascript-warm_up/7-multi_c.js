#!/usr/bin/node
// a script that prints x times “C is fun”

const arg = Number(process.argv[2]);
if (isNaN(arg)) {
    console.log("Missing number of occurrences");
}
else {
    for (let itr = 0; itr < arg; itr++) {
        console.log("C is fun"); }
}