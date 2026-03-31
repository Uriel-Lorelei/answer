#!usr/bin/env bash

kitty -e python3 ~/.config/ansscripts/dictionary.py &
sleep 0.3
hyprctl dispatch focuswindow title:python3
hyprctl dispatch togglefloating
hyprctl dispatch centerwindow
hyprctl dispatch resizeactive exact 300 75
