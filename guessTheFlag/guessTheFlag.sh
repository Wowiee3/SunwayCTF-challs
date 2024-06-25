#!/bin/bash

FLAG="SUNCTF{c4n7_7h1nk_0f_fl46_n4m35}"
echo -n "If you guess the flag correctly, we will let you know!: "
read USER_INPUT

if [[ $FLAG == $USER_INPUT ]]; then
    echo "Correct!"
else
    echo "Wrong..."
fi
