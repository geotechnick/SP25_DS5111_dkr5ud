# get_gainer.py - Main script to execute processing
main_script = """
import sys
from bin.gainers.factory import GainerFactory

class ProcessGainer:
    def __init__(self, gainer_downloader, gainer_normalizer):
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer
    
    def _download(self):
        self.downloader.download()
    
    def _normalize(self):
        self.normalizer.normalize()
    
    def _save_to_file(self):
        self.normalizer.save_with_timestamp()
    
    def process(self):
        self._download()
        self._normalize()
        self._save_to_file()

if __name__ == "__main__":
    choice = sys.argv[1]
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()
    runner = ProcessGainer(downloader, normalizer)
    runner.process()
"""

# Makefile update
makefile = """
gainers:
	python get_gainer.py $(SRC)
"""

files = {
    "bin/gainers/base.py": template,
    "bin/gainers/yahoo.py": yahoo,
    "bin/gainers/wsj.py": wsj,
    "bin/gainers/factory.py": factory,
    "get_gainer.py": main_script,
    "Makefile": makefile,
}

for filename, content in files.items():
    with open(filename, "w") as f:
        f.write(content)

print("Refactored code has been written to the appropriate files.")