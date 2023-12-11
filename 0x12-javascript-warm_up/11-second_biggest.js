#!/usr/bin/node

// A script that sort and find second-largest number in array.

const array_len = process.argv.length

if (array_len <= 3) {
    return (0);
} else {
    const cmd_array = process.argv.map(Number)
    .slice(2, array_len).sort((f, s) => f - s );
    console.log(cmd_array[cmd_array.length - 2]);
}