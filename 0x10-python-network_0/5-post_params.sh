#!/bin/bash
#sends a POST request to a url and displays the body of the response
curl -s -X POST -d "email=test%40gmail%2Ecom&subject=I+will+always+be+here+for+PLD" "$1"
