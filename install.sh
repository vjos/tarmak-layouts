#!/bin/sh

# get parent layout from command line argument
if [ -z "$1" ]
then
  export LAYOUT=gb
else
  export LAYOUT=$1
fi

# create layout file for X11
envsubst < tarmak-x11 > /usr/share/X11/xkb/symbols/tarmak

# add X11 rule for layout
python tarmak-rules.py
