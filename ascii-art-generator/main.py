import sys
from PIL import Image

# ASCII characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def main(new_width=100):
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path> [width]")
        return

    path = sys.argv[1]
    try:
        image = Image.open(path)
    except Exception as e:
        print(e)
        return

    if len(sys.argv) > 2:
        try:
            new_width = int(sys.argv[2])
        except ValueError:
            print("Invalid width provided. Using default 100.")

    new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width)))
    
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    
    print(ascii_image)
    
    # Save to file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
    print("\nASCII art saved to ascii_image.txt")

if __name__ == "__main__":
    main()
