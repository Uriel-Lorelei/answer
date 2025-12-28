import os
import subprocess
import shutil
import time

home_dir = os.path.expanduser("~") # to make it easy for myself
config_dir = os.path.join(home_dir, ".config") # the destination of config files
setup_dir = os.path.join(home_dir, "answer") # cloned directory
directories = ["waybar", "mako", "kitty", "fastfetch", "nwg-look", "hypr", "wofi", "images", "ansscripts"]

# packages to add using pacman
packages = ["mesa", "lib32-mesa", "vulkan-icd-loader", "lib32-vulkan-icd-loader", "linux-headers", "hyprland", "wayland", "tk", "kate", "imagemagick", "base-devel", "yt-dlp", "wl-clip-persist", "zip", "unzip", "polkit", "tar", "xdg-user-dirs", "xdg-user-dirs-gtk", "fzf", "tmux", "upower", "htop", "btop", "libreoffice-fresh", "audacious", "cava", "xdg-desktop-portal", "xdg-desktop-portal-hyprland", "xdg-desktop-portal-gtk", "gvfs", "wl-clipboard", "kitty", "wofi", "waybar", "thunar", "swww", "nwg-look", "power-profiles-daemon", "mako", "network-manager-applet", "mpv", "feh", "code", "pipewire", "pipewire-pulse", "pipewire-alsa", "alsa-utils", "wireplumber", "pavucontrol", "brightnessctl", "ufw", "bluez", "bluez-utils", "blueman", "hyprlock", "hyprshot", "noto-fonts", "noto-fonts-cjk", "noto-fonts-emoji", "ttf-liberation", "ttf-dejavu", "hypridle", "python-sympy", "swayosd", "ly", "libmtp", "gvfs-mtp", "android-udev", "ttf-jetbrains-mono-nerd"]

# packages to add using yay
yay_packs = ["bibata-cursor-theme-bin", "librewolf-bin"]

def install_package(packages: list):
    for package in packages:
        check = subprocess.run(["pacman", "-Q", package], capture_output=True, text=True)
        if check.returncode != 0:
            print(f"Installing --> {package}...")
            install = subprocess.run(["sudo","pacman", "-S", "--noconfirm", package], capture_output=True, text=True)
            if install.returncode == 0:
                print(f"Installed --> {package}!")
            else:
                print(install.stderr)
        else:
            print(f"{package.upper()} is already installed.")

def add_extra_packages(packs: list):
    for p in packs:
        check = subprocess.run(["pacman", "-Q", p], capture_output=True, text=True)
        if check.returncode != 0:
            print(f"Installing --> {p}...")
            install = subprocess.run(["sudo","pacman", "-S", "--noconfirm", p], capture_output=True, text=True)
            if install.returncode == 0:
                print(f"Installed --> {p}!")
            else:
                print(install.stderr)
        else:
            print(f"{p.upper()} is already installed.")

def from_yay(yay_packs):
        for yp in yay_packs:
            install = subprocess.run(["yay", "-S", "--noconfirm", yp], capture_output=True, text=True)
            if install.returncode == 0:
                print(f"Installed --> {yp}.")
            else:
                print(f"ERROR: While installing -{yp}-,this happened:\n{install.stderr}")

def copy(dir):
    for d in dir:    
        os.system(f"cp -r {os.path.join(setup_dir, d)} {config_dir}")

def backup(dir):
    os.makedirs(os.path.join(config_dir, "backup-configs"), exist_ok=True)
    for d in dir:
        if os.path.exists(os.path.join(config_dir, d)):
            shutil.move(os.path.join(config_dir, d), os.path.join(config_dir, "backup-configs"))
        else:
            print(f"{d} not found. Skipping...")

def yay():
    add_yay = input("Do you want to add yay(including librewolf and a mouse cursor theme!)(y/n)\n> ").lower()
    if add_yay in ["yes", "y"]:
        if shutil.which("yay"):
            print("Yay is already added or there is a conflicting command using yay.")
            from_yay(yay_packs)
        else:
            #os.system(f"cd {home_dir} && mkdir -p yay_home && cd yay_home && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si")
            subprocess.run(["git", "clone", "https://aur.archlinux.org/yay.git"], cwd=home_dir)
            subprocess.run(["makepkg", "-si"], cwd=os.path.join(home_dir, "yay"))
            from_yay(yay_packs)
    elif add_yay in ["no", "n"]:
        print("Skipping yay. A lot of packages wont be added.")
    else:
        print("Not a valid answer. Please try again.")
        yay()

def add_ly():
    is_ly = input("Would you like to add ly as your display manager?(y/n)\n> ").lower()
    if is_ly == "y":
        subprocess.run(["sudo", "mv", "/etc/ly/config.ini", "/etc/ly/config_backup"])
        subprocess.run(["sudo", "systemctl", "enable", "ly@tty2.service"])
        subprocess.run(["sudo", "cp", os.path.join(setup_dir, "ly", "config.ini"), "/etc/ly/config.ini"])
    elif is_ly == "n":
        print("Skipping ly...")
    else:
        print("Not a valid answer.")
        add_ly()

# this function just make files executable
def mod(name, dir, category):
    subprocess.run(["chmod", "+x", name], cwd=os.path.join(dir, category))

# function to download gpu
# def gpu():
#     print("What GPU drivers would you like to add?")
#     print("1. Intel\n2. AMD\n3. NVIDIA\n4. I don't trust you. I will do it myself.(skip)")
#     user_ans = int(input("--> "))
#     if user_ans == 1:
#         add_extra_packages(["vulkan-intel", "intel-media-driver"])
#     elif user_ans == 2:
#         add_extra_packages(["vulkan-radeon", "xf86-video-amdgpu", "lib32-vulkan-radeon"])
#     elif user_ans == 3:
#         print("You make have some problems using Nvidia. Be careful.")
#         time.sleep(1)
#         add_extra_packages(["nvidia-open", "nvidia-utils", "nvidia-settings", "egl-wayland"])
#     elif user_ans == 4:
#         print(":( skipping...")
#     else:
#         print("Not a valid answer.")
#         gpu()

functions = [(install_package, (packages,)), (backup, (directories,)), (copy, (directories,)), (yay, ())]
users_packs = []

def main():
    subprocess.run(["sudo", "pacman", "-Syy"])
    
    # perform all downloads and moves the required configs to .config
    for function, args in functions:
        function(*args)
    print("CONFIGS ADDED")
    
    # time.sleep(1)
    # gpu()
    
    # extra_packs = input("Would you like to add some of your own preferred packages?(y/n)\n> ").lower()
    # if extra_packs == "y":
    #     list_extra_packs

    # starts swww daemon so that wallpaper can be changed later
    subprocess.Popen(["swww-daemon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, start_new_session=True)
    
    # sets up sway-osd (responsible for changing volumes and brightness) and changes wallpaper
    subprocess.run(["sudo", "systemctl", "enable", "swayosd-libinput-backend.service"])
    subprocess.run(["sudo", "systemctl", "start", "swayosd-libinput-backend.service"])
    subprocess.Popen(["swayosd-server"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, start_new_session=True)
    time.sleep(1)
    subprocess.run(["swww", "img", os.path.join(config_dir, "images", "wallpapers", "cyber.jpeg"), "--transition-type=center"])
    
    # adds ly if True
    add_ly()

    # making sure the script can run
    mod("waykill.sh", config_dir, "ansscripts")

    # this is a theme for mainly dark mode for gtk apps
    subprocess.run(["git", "clone", "https://github.com/vinceliuice/Graphite-gtk-theme.git"], cwd=home_dir)
    mod("install.sh", home_dir, "Graphite-gtk-theme")
    subprocess.run(["./install.sh", "-c", "dark", "-s", "standard", "-s", "compact", "-l", "--tweaks", "black", "rimless"], cwd=os.path.join(home_dir, "Graphite-gtk-theme"))
    
    #icons missing (may or may not add them later)
    
    # adds zsh and oh my zsh to change the theme of kitty
    yes_zsh = input("Add zsh?(y/n)\n> ").lower()   
    if yes_zsh == "y":
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "zsh"])
        subprocess.run(["sudo", "chsh", "-s", "/bin/zsh"])
        cmd = 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
        subprocess.run(cmd, shell=True)
    elif yes_zsh == "n":
        print("skipping")
    else:
        print("Not a valid answer.")
    
main()