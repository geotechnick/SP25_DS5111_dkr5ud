from abc import ABC, abstractmethod

# base.py - Defines abstract base classes for downloading and processing
template = """
class GainerDownload(ABC):
    def __init__(self, url):
        self.url = url
    
    @abstractmethod
    def download(self):
        pass

class GainerProcess(ABC):
    @abstractmethod
    def normalize(self):
        pass
    
    @abstractmethod
    def save_with_timestamp(self):
        pass
"""
