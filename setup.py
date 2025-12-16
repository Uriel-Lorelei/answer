import os
import subprocess
import shutil
import time

#a = subprocess.run(["nyancat"], capture_output=True, text=True)
#print(a.stdout)
#print(a.stderr)

home_dir = os.path.expanduser("~")
config_dir = os.path.join(home_dir, ".config")
setup_dir = os.path.join(home_dir, "answer")
directories = ["waybar", "mako", "kitty", "fastfetch", "nwg-look", "hypr", "wofi", "wallpapers"]
packages = ["mesa", "hyprland", "wayland", "imagemagick", "base-devel", "wl-clip-persist", "zip", "unzip", "polkit", "tar", "xdg-user-dirs", "xdg-user-dirs-gtk", "fzf", "tmux", "upower", "htop", "btop", "libreoffice-fresh", "audacious", "cava", "xdg-desktop-portal", "xdg-desktop-portal-hyprland", "xdg-desktop-portal-gtk", "gvfs", "wl-clipboard", "kitty", "wofi", "waybar", "thunar", "swww", "nwg-look", "power-profiles-daemon", "mako", "network-manager-applet", "mpv", "feh", "code", "pipewire", "pipewire-pulse", "pipewire-alsa", "alsa-utils", "wireplumber", "pavucontrol", "brightnessctl", "ufw", "bluez", "bluez-utils", "blueman", "hyprlock", "noto-fonts", "noto-fonts-cjk", "noto-fonts-emoji", "ttf-liberation", "ttf-dejavu", "hypridle", "ttf-jetbrains-mono-nerd"]
yay_packs = ["bibata-cursor-theme-bin", "papirus-icon-theme", "papirus-folders", "librewolf-bin"]
is_yay = 0 

def install_package(packages):
    for package in packages:
        check = subprocess.run(["pacman", "-Q", package], capture_output=True, text=True)
        if check.returncode != 0:
            print(f"Installing {package}...")
            install = subprocess.run(["sudo","pacman", "-S", "--noconfirm", package], capture_output=True, text=True)
            if install.returncode == 0:
                print(f"Installed {package}.")
            else:
                print(install.stderr)
        else:
            print(f"{package.upper()} is already installed.")

def from_yay(yay_packs):
        for yp in yay_packs:
            install = subprocess.run(["yay", "-S", "--noconfirm", yp], capture_output=True, text=True)
            if install.returncode == 0:
                print(f"Installed {yp}.")
            else:
                print(install.stderr)

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
    add_yay = input("Do you want to add yay?(y/n)\n> ").lower()
    if add_yay in ["yes", "y"]:
        if shutil.which("yay"):
            print("Yay is already added or there is a conflicting command using yay.")
            from_yay(yay_packs)
        else: #potential problem
            os.system(f"cd {home_dir} && mkdir -p yay_home && cd yay_home && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si")
            from_yay(yay_packs)
    elif add_yay in ["no", "n"]:
        print("Skipping yay. A lot of packages wont be added.")
    else:
        print("Not a valid answer. Please try again.")
        yay()

functions = [(install_package, (packages,)), (backup, (directories,)), (copy, (directories,)), (yay, ())]

def main():
    for function, args in functions:
        function(*args)
    print("CONFIGS ADDED")
    time.sleep(1)
    subprocess.Popen(["swww-daemon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL, start_new_session=True)
    subprocess.run(["swww", "img", os.path.join(config_dir, "wallpapers", "escape_velocity.jpg")])

    os.system(f"cd && git clone https://github.com/vinceliuice/Graphite-gtk-theme.git")
    subprocess.run(["chmod", "+x", "install.sh"], cwd=os.path.join(home_dir, "Graphite-gtk-theme"))
    subprocess.run(["./install.sh", "-c", "dark", "-s", "standard", "-s", "compact", "-l", "--tweaks", "black", "rimless"], cwd="Graphite-gtk-theme")
    subprocess.run(["papirus-folders", "-C", "black"])

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