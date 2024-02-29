#!/bin/bash
#sends a POST request to a specific URL and displays the body of the respons
curl -sX POST -d "email=test@gmail.com&subject=I+will+always+be+here+for+ PLD" "$1"
