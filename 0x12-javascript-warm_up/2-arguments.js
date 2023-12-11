#!/usr/bin/node

// A script that prints a message depending on
// the number of arguments passed

const processArg = process.argv.length;
console.log(processArg === 2 ? 'No argument' : processArg === 3 ? 'Argument found' : 'Argument found');