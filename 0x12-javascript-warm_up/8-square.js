#!/usr/bin/node

// A script that prints a square

const arg = Math.floor(Number(process.argv[2]));
let char_arg = '';

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let arg_num = 0; arg_num < arg; arg_num++) {
    let arg_ds = '';
    for (let itr = 0; itr < arg; itr++) arg_ds += 'X';
    console.log(arg_ds);
  }
}
