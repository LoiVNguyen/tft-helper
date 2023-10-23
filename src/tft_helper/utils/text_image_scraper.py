import cv2
import pytesseract 
import numpy as np
from PIL import ImageGrab, Image


# Returns full PIL Image.
def grab_image() -> Image:
    image = ImageGrab.grab(bbox = None)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    image = Image.fromarray(image)

    return image


# Returns augment round or 0.
def get_augment_round(image: Image) -> int:
    width, height = image.size
    left, top = (height/8) * 4, 0
    right, bottom = (height/8) * 7, (height/16) * 2
    cropped = image.crop((left, top, right, bottom))
    text = _grab_text_from_image(np.array(cropped), True)
    
    return _augment_round(text)


# Helper function to determine augment round.
def _augment_round(text: int) -> int:
    mappings = {'2-2': 2, '3-2': 3, '4-2': 4}
    for i in text.split():
        if i in mappings:
            return mappings[i]
    
    return 0


# Grabs text (augments or round) from image. 
def _grab_text_from_image(image: np.array, check_augment: bool) -> None:
    if check_augment:
        image = cv2.threshold(image, 30, 255, cv2.THRESH_BINARY_INV)[1]
    else:
        image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV)[1]
    
    text = pytesseract.image_to_string(image, lang='eng', config="--psm 11 oem 1")

    return text
