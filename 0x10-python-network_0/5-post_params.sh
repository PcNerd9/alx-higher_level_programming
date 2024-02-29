#!/bin/bash
#sends a POST request to a specific URL and displays the body of the respons
curl -X POST -d "email=test%40gmail%2Ecom&subject=I+will+always+be+here+for+PLD" "$1"
