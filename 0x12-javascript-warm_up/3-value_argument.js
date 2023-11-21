#!/usr/bin/node

// A script that prints the first argument passed to it

const cmd_argument = process.argv[2];
if (cmd_argument)
{
	console.log(cmd_argument);
}
else
{
	console.log("No argument");
}
