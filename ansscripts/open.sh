#!usr/bin/env bash

kitty --title "Dictionary" -e python3 ~/.config/ansscripts/dictionary.py &
# sleep 0.4
hyprctl dispatch focuswindow title:Dictionary
# hyprctl dispatch togglefloating
# hyprctl dispatch centerwindow
# hyprctl dispatch resizeactive exact 300 75
