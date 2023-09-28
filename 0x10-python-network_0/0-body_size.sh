#!/usr/bin/bash
# Takes a url, sends a request to that url, and displays the size og body of response
curl -s -o /tmp/response_body "$1" && echo $(wc -c < /tmp/response_body) && rm -f /tmp/response_body
