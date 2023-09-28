#!/bin/bash
# Takes in a URL  and displays all HTTP  methods the server will accept
curl -sX OPTIONS "$1" -LI -H "Accept: */*" | grep -o "Allow: \s*[^\n]*" | cut -d " " -f 2-
