#!/bin/bash
#displays all http methods the server will accept
curl -sL -X  OPTIONS -I "$1" | grep "Allow:" | cut -d " " -f2-
