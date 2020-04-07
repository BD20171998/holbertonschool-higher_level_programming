#!/bin/bash
# Bash script that takes a URL & displays the size of the body of the response
curl -s -L -I "$1" | grep -i Content-Length | cut -d " " -f2
