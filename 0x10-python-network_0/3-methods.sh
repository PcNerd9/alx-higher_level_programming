#!/bin/bash
#displays all http methods the server will accept
curl -sXI OPTIONS "$1"
