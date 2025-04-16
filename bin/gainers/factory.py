# factory.py - Factory pattern for object selection
from .yahoo import GainerDownloadYahoo, GainerProcessYahoo
from .wsj import GainerDownloadWSJ, GainerProcessWSJ

class GainerFactory:
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj'], f"Unrecognized gainer type {choice}"
        self.choice = choice
    
    def get_downloader(self):
        return GainerDownloadYahoo() if self.choice == 'yahoo' else GainerDownloadWSJ()
    
    def get_processor(self):
        return GainerProcessYahoo() if self.choice == 'yahoo' else GainerProcessWSJ()
