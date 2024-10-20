#!/bin/zsh

# Exchange the values of the return value to 1 if you want to execute the else in the code
k=0
if $k; then
echo "I'm about to run Shhbot for you!"
echo ""
cd /Users/yann/Desktop/MyBot/MyBot/src
python3 main.py

else

echo "I'm going to push changes to your git"

cd /Users/yann/Desktop/MyBot/MyBot
git pull
git add --all
git commit -m "Adding a shell script to try"

fi