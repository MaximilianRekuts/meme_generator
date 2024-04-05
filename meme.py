import os
import random
import argparse
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

def generate_meme(path=None, body=None, author=None):
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = [os.path.join(root, name) for root, _, files in os.walk(images) for name in files]
        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = [quote for f in quote_files for quote in Ingestor.parse(f)]
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Meme Generator")
    parser.add_argument('--path', type=str, help="Path to an image file")
    parser.add_argument('--body', type=str, help="Quote body to add to the image")
    parser.add_argument('--author', type=str, help="Quote author to add to the image")
    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
