#!/bin/bash

FLAG=sunctf{[REDACTED]}

echo -n "If you guess the flag correctly, we will let you know!: "
read USER_INPUT

if [[ $FLAG == $USER_INPUT ]]; then
    echo "Correct!"
else
    echo "Wrong..."
fi
