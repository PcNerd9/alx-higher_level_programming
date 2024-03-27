#!/bin/bash
#sends a GET requests to the URL and displays the body of the response
curl -sI -X GET "$1" | grep -q 200 && curl -s "$1"
