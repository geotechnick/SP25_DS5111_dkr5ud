from abc import ABC, abstractmethod

# Base class for the gainer processing logic
class GainerBase(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def download(self):
        """Abstract method for downloading gainer data."""
        pass

    @abstractmethod
    def normalize(self):
        """Abstract method for normalizing gainer data."""
        pass

    @abstractmethod
    def save_with_timestamp(self):
        """Abstract method for saving gainer data with a timestamp."""
        pass