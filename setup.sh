#!/bin/bash

# Update the Apt to prevent future apt errors 
sudo apt update

# Install package managers
sudo apt install -y snapd aptitude flatpak
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# Asking permission for plugins
read -p "Do you want to install KDE plugins for flatpak? [Y/n] " kdechoice

if [[ "$kdechoice" =~ [Yy] || -z "$kdechoice" ]]; then
    sudo apt install -y plasma-discover-backend-flatpak
else
    read -p "Would you like to install GNOME addon for flatpak? [Y/n] " gnomechoice
    
    if [[ "$gnomechoice" =~ [Yy] || -z "$gnomechoice" ]]; then
        sudo apt install -y gnome-software-plugin-flatpak
    else
        echo "Setup completed successfully. Please restart your computer for better experience."
    fi
fi
#Make shortcut for console
sudo curl -L https://raw.githubusercontent.com/mystic-poop/PMFD/main/pmfd.py -o /usr/local/bin/pmfd
sudo chmod +x /usr/local/bin/pmfd