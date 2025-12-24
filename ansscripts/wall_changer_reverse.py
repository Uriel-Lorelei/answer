import subprocess
import os
import re

# this code is to change the wallpaper
# in alphabetical order!!!

# giving the directory a variable
home_dir = os.path.expanduser("~")
wall_path = os.path.join(home_dir, ".config", "images", "wallpapers")
ansscripts = os.path.join(home_dir, ".config", "ansscripts")
hyprlock_path = os.path.join(home_dir, ".config", "hypr", "hyprlock.conf")

# getting the list of wallpapers and sorting them alphabetically
wallpapers = os.listdir(wall_path)
wallpapers.sort(reverse=True)

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
if wall_list == []:
    wall_list = wallpapers
    subprocess.run(["swww", "img", os.path.join(wall_path, wall_list[0]), "--transition-type=center"])
else:
    subprocess.run(["swww", "img", os.path.join(wall_path, wall_list[0]), "--transition-type=center"])

# copies the current wallpaper to another folder and renames it so that it can be used in hyprlock
os.system("rm -rf ~/.config/ansscripts/lock_screen/*")
subprocess.run(["cp", os.path.join(wall_path, wall_list[0]), os.path.join(ansscripts, "lock_screen")])

# this gets the extension and copies it with its actual extension 
extension = os.path.splitext(wall_list[0])[1].lower()
subprocess.run(["mv", os.listdir(os.path.join(ansscripts, "lock_screen"))[0], f"current-wall{extension}"], cwd=os.path.join(ansscripts, "lock_screen"))

# changes the hyprlock background
curr_wall = os.listdir(os.path.join(ansscripts, "lock_screen"))
pre_wall = ["current-wall.png", "current-wall.jpg", "current-wall.jpeg", "current-wall.webp"]

with open(hyprlock_path, "r") as f:
    data = f.read()

for word in pre_wall:
    if word in data:
        data = data.replace(word, curr_wall[0])

with open(hyprlock_path, "w") as f:
    f.write(data)