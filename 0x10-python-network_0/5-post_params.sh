#!/bin/bash
# Sends a POST request to the passed URL, and display the body of the respomse
curl -s -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
