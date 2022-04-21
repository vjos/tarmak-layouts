# tarmak-layouts
Tarmak keyboard layouts for X11

Tarmak is a system for transitioning from QWERTY to COLEMAK. Please see [this post](https://forum.colemak.com/topic/1858-learn-colemak-in-steps-with-the-tarmak-layouts/) for more information.

This code is tested on Arch Linux with X11/dwm.

## X11 Usage 
### Installation
Run the install script with elevated permissions, specifying the parent layout:
`sh install.sh gb`

### Switching layouts
Switch to tarmak#1 layout:
`setxkbmap -layout tarmak`

Switch to another tarmak#n:
`setxkbmap -layout tarmak n`

Example with xkb options:
`setxkbmap -layout tarmak 3 -option caps:swapescape -option lv3:ralt_alt`

### Set layout
To use a layout automatically after logging in, simply add the desired command to ~/.xinitrc
