#!/usr/bin/node

// Check if a valid number is provided as a command line argument
const inputNumber = process.argv[2];

if (isNaN(inputNumber) || inputNumber === undefined) {
  console.log('Not a valid number');
} else {
  const parsedNumber = parseInt(inputNumber);
  console.log('My number:', parsedNumber);
}
