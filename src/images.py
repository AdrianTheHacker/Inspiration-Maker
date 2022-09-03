import requests
from dotenv import load_dotenv

from os import getenv, remove

from constants import IMAGE_PATH


load_dotenv()
unsplash_access_key = getenv("UNSPLASH_ACCESS_KEY")


def __clear_image_cache():
    """
    Clears image cache to prevent issues with file writing.
    """
    try:
        remove(IMAGE_PATH)

    except FileNotFoundError:
        pass # You can't delete a file that doesn't exist
    

def get_image():
    """
    Grabs an image from the API and saves it in the image_cache
    """
    __clear_image_cache()

    # Grabs the link to a random image.
    response1 = requests.get(f"https://api.unsplash.com/photos/random/?client_id={unsplash_access_key}")
    regular_image_link = response1.json()["urls"]["regular"]

    # Converts the image link into bytes.
    # Writes the bytes to the image file.
    image_data = requests.get(regular_image_link).content
    with open(IMAGE_PATH, 'wb') as handler:
        handler.write(image_data)
