#!/bin/bash
#takes in a url, sends a request to that url
curl -s "$1" | wc -c
