#!/bin/bash
#sends a GET requests to the URL and displays the body of the response
curl -sI "$1" | grep -q 200 && curl -s "$1"
