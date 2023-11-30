#!/usr/bin/node

// A script that prints the first argument passed to it

const cmdArgument = process.argv[2];

if (cmdArgument) {
    console.log(cmdArgument);
} else {
    console.log("No argument");
}
