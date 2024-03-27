#!/bin/bash
#displays all http methods the server will accept
curl -sX OPTION "$1"
