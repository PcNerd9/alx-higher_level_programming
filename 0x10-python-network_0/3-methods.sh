#!/bin/bash
#takes a specific url and displays all HTTP methods the server accept
curl -sI -X OPTIONS "$1" | cut -d "," -f 2- | cut -d " " -f 2-
