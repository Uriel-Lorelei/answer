import subprocess
import os
import random

home_dir = os.path.expanduser("~")
wall_path = os.path.join(home_dir, ".config", "images", "wallpapers")
# wall_path = os.path.join(home_dir, "config", "images", "wallpapers")

wallpaper = random.choice(os.listdir(wall_path))
subprocess.run(["swww", "img", os.path.join(wall_path, wallpaper)])