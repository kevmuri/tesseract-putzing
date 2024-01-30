import pyautogui
import pytesseract
from PIL import Image
from pytesseract import Output

# Add path to tesseract.exe file here
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Capture a screenshot
screenshot = pyautogui.screenshot()

# Save the image (you can delete the image after text detection)
screenshot.save("screenshot.png")

# Open the image file
img = Image.open("screenshot.png")

# Use pytesseract to convert the image to plain text
screenshot_as_data = pytesseract.image_to_data(img, output_type=Output.DICT)

# Define a word you're looking for
word = "Tools"

# Search if the word is found in the recognized text
if word in screenshot_as_data['text']:
    # Get all indexes of the word
    word_indexes = [i for i, txt in enumerate(screenshot_as_data['text']) if txt == word]

    # Click on all found word locations
    for word_index in word_indexes:
        x, y, w, h = screenshot_as_data['left'][word_index], screenshot_as_data['top'][word_index], screenshot_as_data['width'][word_index], screenshot_as_data['height'][word_index]
        pyautogui.click(x + w/2, y + h/2)