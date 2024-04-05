import os
import random
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel

def setup():
    """Load all resources and return random image and quote."""
    # Paths
    images_path = "./_data/photos/"
    simple_lines_path = "./_data/SimpleLines/"
    dog_quotes_path = "./_data/DogQuotes/"
    
    # Loading Images
    imgs = []
    for root, _, files in os.walk(images_path):
        imgs.extend([os.path.join(root, name) for name in files if name.endswith(('.png', '.jpg', '.jpeg'))])

    # Preparing Quote Files List
    quote_files = []
    for path in [simple_lines_path, dog_quotes_path]:
        for root, _, files in os.walk(path):
            quote_files.extend([os.path.join(root, name) for name in files if name.endswith(('.txt', '.docx', '.pdf', '.csv'))])

    # Using the Ingestor class to parse all quote files
    quotes = []
    for file in quote_files:
        try:
            quotes.extend(Ingestor.parse(file))
        except Exception as e:  # Generic exception handling, adjust as needed
            print(f"Error processing file {file}: {e}")

    return quotes, imgs

def select_random_quote_and_image(quotes, imgs):
    """Selects a random quote and image."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    return img, quote

def main():
    quotes, imgs = setup()
    img, quote = select_random_quote_and_image(quotes, imgs)
    # Now you have a random img and quote to use for meme generation
    # Implement the meme generation logic here, utilizing img and quote

if __name__ == "__main__":
    main()
