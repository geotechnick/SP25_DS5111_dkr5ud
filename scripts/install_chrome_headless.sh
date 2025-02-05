sudo apt update
sudo apt install fonts-liberation -y
sudo wget --no-clobber https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb -y
sudo apt --fix-broken install
sudo apt install ./google-chrome-stable_current_amd64.deb -y

# Check Version of chrome and run a quick sanity check
google-chrome-stable --version
google-chrome-stable --headless --disable-gpu --dump-dom https://example.com/


