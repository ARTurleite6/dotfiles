#!/bin/sh
set -e 
i3lock --nofork --show-failed-attempts --ignore-empty-password --tiling --image='/path/to/img.png' 
xset dpms
