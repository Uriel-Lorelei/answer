This is an extremely basic hyprland configuration.
Made for my own personal use.

In order to use this configuration, first do the following command in the terminal:
> git clone https://github.com/Uriel-Lorelei/answer.git

Then you can run the script by going to the answer directory and running:
> python3 setup.py

And that's it.
Although you may have to put your password mutiple times.

Make sure to use this configuration on fresh hyprland install. Although there shouldn't be much problem when using this on an already configured hyprland.

This configuration uses waybar, mako, wofi, kitty, swayosd, and nwg-look for configuration. 
Most of the configurations done are just basic changes and there are only few external additions.
Wallpapers are mostly from another pre-configuration of Hyprland called Hyde and others are my own addition found on the Internet.

The default browser on this configuration is librewolf. There is chance that it isn't added. If it hasn't do:
> yay -S librewolf-bin

If you like to use another browser, change the default browser in '.config/hypr/hyprland.conf' after downloading one.

To change the wallpaper, you can do: 'SUPER + SHIFT + right arrow key' which randomly changes the wallpaper and you can do 'SUPER + R' to reload waybar.

In order to change to dark-mode, you can open nwg-look to change to theme downloaded from Graphite-gtk-theme.
