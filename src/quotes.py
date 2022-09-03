# Module used to grab quotes

from dataclasses import dataclass
import requests

import random


@dataclass
class Quote:
    """
    Custom object to represent a quote.
    """

    message: str
    author: str


MAX_RANGE = 100 # When grabbing a quote, the API returns a list of quotes.
                # In order to pick a random quote, we grab 100 quotes and choose
                # a random one.
                #
                # An alternative could be to choose a random number of quotes, and always 
                # grab the last one. This way when grabbing quotes such as the first, second
                # or third one, you don't have to load 50+ quotes.


def get_quote(max_range=MAX_RANGE) -> Quote:
    """
    Grabs a random quote from the quote API 
    and returns a Quote object out of the information.
    """

    response = requests.get(f"https://programming-quotes-api.herokuapp.com/Quotes?count={MAX_RANGE}")
    quotes_list = response.json()

    quote_index = random.randint(1, 100)

    return Quote(quotes_list[quote_index]["en"],
                 quotes_list[quote_index]["author"])
