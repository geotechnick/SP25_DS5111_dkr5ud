PROJECT_ROOT := $(shell pwd)

# Default target
default:
	@cat makefile

# Virtual environment setup
env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

# Update dependencies
update: env
	. env/bin/activate; pip install -r requirements.txt

# Linting
lint:
	pylint bin/gainers/factory.py

# Run tests
test:
	pytest tests/

# Fetch Yahoo gainers
ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	python -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

# Fetch WSJ gainers
wjsgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=500 https://www.wsj.com/market-data/stocks/us/movers > wjsgainers.html

wjsgainers.csv: wjsgainers.html
	python -c "import pandas as pd; raw = pd.read_html('wjsgainers.html'); raw[0].to_csv('wjsgainers.csv')"

# Run Gainer Processing
gainers:
	python get_gainer.py $(SRC)

