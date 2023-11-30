#!/usr/bin/node

// A script that displays given string

const arg = Math.floor(Number(process.argv[2]));

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let itr = 0; itr < arg; itr++) {
    console.log('C is fun');
  }
}