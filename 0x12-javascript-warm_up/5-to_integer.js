#!/usr/bin/node

// The above line is a shebang, specifying that this script should be run using Node.js

// Extract the command-line argument, convert it to a number, and round it down

const cmd_arg = Math.floor(Number(process.argv[2]));

// Check if the converted number is NaN (Not a Number)

if (isNaN(cmd_arg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${cmd_arg}`);
}
