#!/bin/bash

# Update package list
sudo apt update

# Upgrade installed packages
sudo apt upgrade -y

# Upgrade distribution (if needed)
sudo apt dist-upgrade -y

# Remove unnecessary packages
sudo apt autoremove -y
