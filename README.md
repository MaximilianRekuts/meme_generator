Meme Generator
This project creates dynamic memes by overlaying quotes on images. It can automatically select a random image and quote, or users can specify their own image and quote through a command-line interface or a Flask web application.

Overview
The project consists of two main modules:

Quote Engine: Extracts quotes from a variety of file formats and organizes them as Quote objects.
Meme Engine: Generates memes by combining quotes and images. It allows for custom input via a command-line interface or a web interface.
Project Setup
Follow these steps to set up and run the project locally.

Clone the Repository

```
git clone https://github.com/yourusername/meme-generator.git
cd meme-generator
```

Install Dependencies
PDF Ingestion: Install pdftotext for PDF file processing. Download it from here and add it to your system's PATH.

Python Environment: Create and activate a virtual environment:

With venv:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Or with Conda:

conda create --name memeenv python=3.8
conda activate memeenv

Install Required Packages:

pip install -r requirements.txt

Usage
Generate a Random Meme
To generate a random meme, simply run:

python main.py

Generate a Custom Meme
To generate a meme with custom parameters, use:

python main.py --body "A quote body" --author "Author Name" --image_path "path/to/image.jpg"

For help:

python main.py -h

Web Interface
Run the Flask app to generate memes through a web interface:

python app.py

Navigate to http://127.0.0.1:5000 in your web browser.

Modules Description
Quote Engine: Contains classes for ingesting quotes from different file formats, including CSV, DOCX, PDF, and TXT.
Meme Engine: Handles image manipulation tasks such as resizing and adding text to images.
Running Tests
Ensure your code's integrity with:

python -m unittest

Deployment
(Optional) Deploy the Flask app to a platform like Heroku for public access.

Contributions
Contributions are welcome. Please follow the standard fork-pull request workflow.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to Udacity for the project idea and guidelines.
