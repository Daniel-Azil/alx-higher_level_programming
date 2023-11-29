#!/usr/bin/node
// The above line is a shebang, specifying that this script should be run using Node.js

// Extract the command-line argument, convert it to a number, and round it down
const cmd_arg = Math.floor(Number(process.argv[2]));

// Check if the converted number is NaN (Not a Number)
if (isNaN(cmd_arg)){
    // Print a message if the argument is not a valid number
    console.log(`Not a number`)
}
else{
    // Print the converted number if it's a valid number
    console.log(`My number: ${cmd_arg}`);
}