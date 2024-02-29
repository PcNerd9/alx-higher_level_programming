#!/usr/bin/env bash
#takes in a url, sends a request to that url
#and displays the size of the body of the response


if [ $# -lt 1 ];
then
	echo "Usage: $0 <URL>"
	exit 1
fi;

url=$1

response_file=$(mktemp)
if ! curl -s -o "$response_file" "$url";
then
	echo "Failed to get the url"
fi;

size=$(wc -c < "$response_file")

echo "$size"
