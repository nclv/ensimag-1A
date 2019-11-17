#!/bin/sh

last | head -n -2 | cut -f 1 -d ' ' | sort | uniq -c | sort -n
