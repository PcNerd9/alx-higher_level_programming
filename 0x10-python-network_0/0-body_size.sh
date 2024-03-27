#!/bin/bash
#sends a request to a url passed and display the size of the body
curl -s "$1" | wc -c
