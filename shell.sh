#!/bin/bash
# number_guess.sh

secret_number=$(( RANDOM % 10 + 1 ))
guess=0

echo "Guess a number between 1 and 10"

while [[ $guess -ne $secret_number ]]; do
  read -p "Enter your guess: " guess
  if [[ $guess -lt $secret_number ]]; then
    echo "Too low!"
  elif [[ $guess -gt $secret_number ]]; then
    echo "Too high!"
  else
    echo "Congratulations! You guessed it!"
  fi
done
