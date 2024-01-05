from PIL import Image
import time
from colorama import Fore
import os
import termcolor
import webcolors
def print_image(image_path):
    image = Image.open(image_path)
    width, height = image.size
    aspect_ratio = height / width * 0.5  # Adjust aspect ratio based on your console font
    new_width = 80  # Set the desired width for the ASCII art
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    grayscale_image = resized_image.convert("L")  # Convert image to grayscale
    ascii_chars = "@%#*+=- . "  # Use ASCII characters for representing different shades

    ascii_art = ""
    for y in range(new_height):
        for x in range(new_width):
            pixel_value = grayscale_image.getpixel((x, y))
            index=int(pixel_value/255*(len(ascii_chars)-1))
            char=ascii_chars[index]
            pixel_color=resized_image.getpixel((x,y))
            ansi=16+(pixel_color[0]//16)*36+(pixel_color[1]//16)*6+(pixel_color[2]//16)
            char_color=f"\x1b[38;5;{ansi}m"
            #clo=webcolors.rgb_to_name(pixel_color)
            #ansi=colorama.Fore.__dict__.get(clo.upper())
            #char_color=getattr(colorama.Fore,ansi) if ansi else ""
            ascii_art+=f"{char_color}{char}"
        ascii_art += "\n"
    print(ascii_art)
#print(__name__)
if __name__=="__main__":
    print_image("main.ico")
    os.system("pause")
