import random
import os
import requests
from flask import Flask, render_template, request
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')

def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        try:
            quotes += Ingestor.parse(file)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            print("Make sure the 'pdftotext' command is installed and accessible in PATH.")
        except ValueError as e:
            print(f"Error: {e}")

    quotes = [q for q in quotes if q is not None]

    images_path = "./_data/photos/dog/"
    imgs = [os.path.join(images_path, filename) for filename in os.listdir(images_path)]

    return quotes, imgs

quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)

@app.route('/create', methods=['GET'])
def meme_form():
    """Display form for meme creation."""
    return render_template('meme_form.html')

@app.route('/create', methods=['POST'])
def meme_post():
    """Handle creation of a meme with user input."""
    image_url = request.form['image_url']
    response = requests.get(image_url)

    local_img = f'temp{random.randint(0, 1000)}.png'
    with open(local_img, 'wb') as fid:
        fid.write(response.content)

    quote_body = request.form['body']
    quote_author = request.form['author']

    path = meme.make_meme(local_img, quote_body, quote_author)
    os.remove(local_img)

    return render_template('meme.html', path=path)

if __name__ == "__main__":
    app.run(debug=True)
