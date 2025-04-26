from bin.gainers.factory import GainerFactory
import sys

if __name__ == "__main__":
    # Read command-line argument for the gainer type (e.g., 'yahoo')
    choice = sys.argv[1]  # e.g., 'yahoo'

    # Create a factory instance based on the user's choice
    factory = GainerFactory(choice)

    # Get the appropriate gainer instance
    gainer = factory.get_gainer()

    # Process the gainer (download, normalize, save)
    gainer.download()
    gainer.normalize()
    gainer.save_with_timestamp()
