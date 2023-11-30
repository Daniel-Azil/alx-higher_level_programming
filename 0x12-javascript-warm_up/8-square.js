#!/usr/bin/node
// A script that prints a square

arg = Math.floor(Number(process.argv[2]));
let char_arg = '';

if (isNaN(arg)) {
    console.log('Missing size');
} else {
    for (let arg_num =0; arg_num < arg; arg_num++){
        char_arg += 'X';
    }
    console.log(char_arg);
}