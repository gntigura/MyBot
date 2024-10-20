#!/bin/zsh

# Exchange the value of the return to 1 if you want to execute the else in the code
if ./return 1; then
echo "I'm about to run Shhbot for you!"
echo ""
cd /Users/yann/Desktop/MyBot/MyBot/src
python3 main.py

else

echo "I'm going to push changes to your git"
echo "-------------------------------------"

cd /Users/yann/Desktop/MyBot/MyBot
git pull
git add --all
git commit -m "fixing issues"

fi