from PIL import Image, ImageDraw, ImageFont
import random
import os


class MemeEngine:
    """A class for generating memes by adding text to images."""

    def __init__(self, output_dir: str):
        """
        Initialize the MemeEngine.

        Parameters:
        - output_dir (str): The directory where generated memes will be saved.
        """
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def make_meme(self, img_path: str, text: str, author: str, max_width=500) -> str:
        """
        Generate a meme by adding text to an image.

        Parameters:
        - img_path (str): The path to the input image file.
        - text (str): The main text to be added to the image.
        - author (str): The author of the quote.
        - max_width (int): The maximum width of the generated image.

        Returns:
        - str: The path to the generated meme image.
        """
        try:
            # Open the input image file
            with Image.open(img_path) as img:
                # Calculate the height while maintaining the aspect ratio
                ratio = max_width / float(img.size[0])
                height = int(ratio * float(img.size[1]))

                # Resize the image
                img = img.resize((max_width, height))

                # Initialize the drawing context
                draw = ImageDraw.Draw(img)

                # Load font
                font_path = os.path.normpath('./font/Open_Sans/OpenSans-VariableFont_wdth,wght.ttf')
                font = ImageFont.truetype(font_path, 20)

                # Determine text position
                text_x = random.randint(10, max_width - 200)
                text_y = random.randint(10, height - 50)

                # Add text to the image
                draw.text((text_x, text_y), text, font=font, fill='white')
                draw.text((text_x, text_y + 25), f"- {author}", font=font, fill='white')

                # Generate a random filename and save the image
                output_file = os.path.join(self.output_dir, f"{random.randint(1, 1000)}.png")
                img.save(output_file)

                return output_file
        except OSError as e:
            raise Exception(f"Error processing image: {e}")
