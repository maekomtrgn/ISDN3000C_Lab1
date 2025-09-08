import sys
from PIL import Image
from rich.console import Console
from rich.text import Text

# Initialize Rich console
console = Console()

# Define the character ramp from darkest to brightest
ASCII_CHARS = ".:-=+*#%@"

def resize_and_grayscale(image, new_width=100):
    # Get current width and height
    width, height = image.size
    
    # Calculate new height maintaining aspect ratio
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    
    # Resize the image
    resized_image = image.resize((new_width, new_height))
    
    # Convert to grayscale
    grayscale_image = resized_image.convert('L')
    
    return grayscale_image

def map_pixel_to_char(pixel_value, pixel_color=None):
    # Make sure pixel_value is in range 0-255
    pixel_value = max(0, min(pixel_value, 255))
    
    # Calculate which character to use
    num_chars = len(ASCII_CHARS)
    char_index = int((pixel_value / 255) * (num_chars - 1))
    char = ASCII_CHARS[char_index]
    
    if pixel_color:
        # Create a Rich Text object with the character and its color
        return Text(char, style=f"rgb({pixel_color[0]},{pixel_color[1]},{pixel_color[2]})")
    return char

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <image_path>")
        return

    try:
        image_path = sys.argv[1]
        image = Image.open(image_path)
        print(f"Successfully opened image: {image_path}")
        print(f"Image size: {image.size}")
        print(f"Image mode: {image.mode}")
        
        print("\nProcessing image...")
        
        # Convert image to ASCII art
        print("\nConverting to ASCII art...")
        
        # Keep the original image for color
        color_image = image.resize((100, int(100 * (image.height / image.width))))
        
        # Convert to grayscale for character mapping
        processed_image = resize_and_grayscale(image)
        
        # Get pixel data from both images
        gray_pixels = processed_image.getdata()
        color_pixels = color_image.getdata()
        
        # Convert pixels to colored ASCII characters
        ascii_chars = [map_pixel_to_char(gray, color) 
                      for gray, color in zip(gray_pixels, color_pixels)]
        
        # Print the ASCII art line by line
        print("\nHere's your ASCII art:")
        width = processed_image.width
        for i in range(0, len(ascii_chars), width):
            # Create a line of text
            line = Text()
            for char in ascii_chars[i:i+width]:
                line.append(char)
            console.print(line)
        
    except FileNotFoundError:
        print(f"Error: Could not find image file: {image_path}")
        return
    except Exception as e:
        print(f"Error: {str(e)}")
        return


if __name__ == "__main__":
    main()