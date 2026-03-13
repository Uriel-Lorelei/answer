import subprocess
import os
import shutil

def systemd_files(file):
    from setup import config_dir, setup_dir
    systemd_dir = os.path.join(config_dir, "systemd", "user")
    os.makedirs(systemd_dir, exist_ok=True)
    shutil.move(os.path.join(setup_dir, "extra", file), systemd_dir)

    subprocess.run(["systemctl", "--user", "daemon-reload"], capture_output=True)
    subprocess.run(["systemctl", "--user", "enable", file], capture_output=True)
    subprocess.run(["systemctl", "--user", "start", file], capture_output=True)

def zsh_setup():
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