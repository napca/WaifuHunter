#!/bin/bash
curl -A "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0" -L 'https://images.google.com/searchbyimage?image_url='$URL 2>/dev/null | egrep -o 'value=..*?.*"Search"'| cut -d \" -f 2
