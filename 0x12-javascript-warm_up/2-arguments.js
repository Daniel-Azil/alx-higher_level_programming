#!/usr/bin/node

// A script that prints a message depending of
// the number of arguments passed

const process_arg = process.argv.length;
if (process_arg == 2)
{
	console.log("No argument");
}
else 
{
	console.log("Argument found");
}
