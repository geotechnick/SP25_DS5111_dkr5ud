#!/bin/bash
set -e

echo "Updating package list..."
sudo apt update

echo "Installing necessary packages..."
sudo apt install -y make python3.12-venv tree wget

echo "Installing Google Chrome Stable..."
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update
sudo apt install -y google-chrome-stable

echo "Setup complete!"