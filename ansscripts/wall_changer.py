import subprocess
import os
import re

# this code is to change the wallpaper
# in alphabetical order!!!

# giving the directory a variable
home_dir = os.path.expanduser("~")
wall_path = os.path.join(home_dir, ".config", "images", "wallpapers")

# getting the list of wallpapers and sorting them alphabetically
wallpapers = os.listdir(wall_path)
wallpapers.sort()

# swww query gets the current wallpaper and search gets the exact name of the wallpaper
check = subprocess.run(["swww", "query"], capture_output=True, text=True)
search = re.search(r'(?<=wallpapers/).*', check.stdout) # gives everything after 'wallpapers/'

# a is the index number from the list of wallpapers + 1
a = wallpapers.index(search.group(0)) + 1

# the wall_list gets the name of wallpapers after the current wallpaper
wall_list = []
for w in range(len(wallpapers)):
    try:
        wall_list.append(wallpapers[a + w])
    except IndexError:
        pass

# changes the wallpaper!
subprocess.run(["swww", "img", os.path.join(wall_path, wall_list[0]), "--transition-type=center"])