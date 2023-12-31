import re
import cv2
import pytesseract 
import numpy as np
from PIL import ImageGrab, Image
from .website_scraper import grab_augments_table, convert_augments_data, LOLCHESS


# Returns full PIL Image.
def get_image() -> Image:
    image = ImageGrab.grab(bbox = None)
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    image = Image.fromarray(image)

    return image


# Returns augment round or 0.
def get_augment_round(image: Image) -> int:
    width, height = image.size
    left, top = (width/8) * 3, 0
    right, bottom = (width/8) * 4, (height/16) * 2
    cropped = image.crop((left, top, right, bottom))
    text = _get_text_from_image(np.array(cropped), True)

    return _augment_round(text)


# Helper function to determine augment round.
def _augment_round(text: int) -> int:
    mappings = {'2-1': 2, '3-2': 3, '4-2': 4}
    for i in text.split():
        if i in mappings:
            return mappings[i]
    
    return 0


# Returns augments shown and their information. 
def get_augments(image: Image) -> list[str]:
    width, height = image.size
    left, top = (width/16) * 3, (height/3) * 1
    right, bottom = (width/16) * 13, (height/24) * 13
    cropped = image.crop((left, top, right, bottom))
    text = _get_text_from_image(np.array(cropped), False)

    return _get_augments_data(text)


# Gets augment data from lolchess given text found from augment round.
def _get_augments_data(text: str) -> list[str]:
    data = convert_augments_data(grab_augments_table(LOLCHESS))
    text = text.replace("+", "Plus")
    text = text.replace("!", " I")
    text = text.replace("|", "I")
    text = text.replace("Ill", "III")
    text = text.replace("Il", "II")
    found = []
    for augment in data:
        pattern = r"\b{}\b".format(augment)
        pattern = re.compile(pattern)
        
        match = re.search(pattern, text)
        if match:
            found.append((augment, match.start()))

    found.sort(key=lambda x: x[1])
    augments = [(augment[0], data[augment[0]]) for augment in found]

    return augments
            

# Grabs text (augments or round) from image. 
def _get_text_from_image(image: np.array, check_augment: bool) -> None:
    if check_augment:
        image = cv2.threshold(image, 30, 255, cv2.THRESH_BINARY_INV)[1]
        text = pytesseract.image_to_string(image, lang='eng', config="--psm 11")
    else:
        image = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY_INV)[1]
 
        text = pytesseract.image_to_string(image, lang='eng', config="--psm 6, oem 1")
    print(text)
    return text
