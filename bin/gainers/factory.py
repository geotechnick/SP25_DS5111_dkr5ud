from yahoo import GainerYahoo

# Factory class to return the correct downloader and processor
class GainerFactory:
    def __init__(self, choice):
        assert choice in ['yahoo'], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_gainer(self):
        """Return the appropriate gainer based on the choice."""
        if self.choice == 'yahoo':
            return GainerYahoo(url="https://yahoo.com")