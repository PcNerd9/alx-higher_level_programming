#!/bin/bash
#takes in a url and sends a GET request to the url
curl -X GET -sH "X-School-User-Id=98" "$1"
