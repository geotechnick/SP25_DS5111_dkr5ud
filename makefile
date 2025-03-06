PROJECT_ROOT := $(shell cd .. && pwd)

default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r $(PROJECT_ROOT)/requirements.txt
	# I think PROJECT_ROOT is not working, the github action is failing to find requirements.txt.
	# I think it'd be safe to assume the makefile will be called from the root of your repo
	# so you can probably just leave that out.

lint:
	pylint normalize_csv.py

test: env
	pylint bin/normalize_csv.py
	pytest tests/test_lab4.py

ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	python -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

wjsgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=500 https://www.wsj.com/market-data/stocks/us/movers > wjsgainers.html

wjsgainers.csv: wjsgainers.html
	python -c "import pandas as pd; raw = pd.read_html('wjsgainers.html'); raw[0].to_csv('wjsgainers.csv')"
