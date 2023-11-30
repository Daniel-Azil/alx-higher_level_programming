#!/usr/bin/node

// A script that prints a message depending on
// the number of arguments passed

const processArg = process.argv.length;
if (processArg === 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}