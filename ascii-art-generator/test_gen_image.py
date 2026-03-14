from PIL import Image, ImageDraw

def create_sample_image():
    img = Image.new('RGB', (100, 100), color = 'red')
    d = ImageDraw.Draw(img)
    d.text((10,10), "Hello", fill=(255,255,0))
    img.save('sample.png')

if __name__ == "__main__":
    create_sample_image()
