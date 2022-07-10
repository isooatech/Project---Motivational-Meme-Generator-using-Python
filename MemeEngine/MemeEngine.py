from PIL import Image, ImageDraw, ImageFont

class make_meme():


    """Create a Postcard With a Text Greeting

    Arguments:
        img_path {str} -- the file location for the input image.
        text {str} -- A quote for an author
        author {str} -- The author of the quote.
        width {int} -- The pixel width value. Default=None.
    Returns:
        str -- the file path to the output image.
    """

    def __init__(self, img_path, text, author, width = 500) -> str:
        self.img_path = img_path
        self.img = Image.open(img_path)
        self.message = f'Quote: {text} by Author: {author}'
        self.width = width

    def resize_img(self):
        ratio = self.width/float(self.img.size[0])
        height = int(ratio*float(self.img.size[1]))
        self.img = self.img.resize((self.width, height), Image.NEAREST)

    def input_text(self):
        draw = ImageDraw.Draw(self.img)
        font = ImageFont.truetype('./fonts/WaterBrush-Regular.ttf', size=20)
        draw.text((10, 30), self.message, font=font, fill='white')

    def save_file(self):
        self.img.save(self.img_path)

