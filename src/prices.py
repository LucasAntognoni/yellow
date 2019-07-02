import os
import requests
import pandas as pd

from configs import EMAIL, TOKEN, PRICE_ENDPOINT_URL


def get_prices_page(page=0):
        
    headers = {'Auth': EMAIL + ":" + TOKEN}

    try:
        response = requests.get(PRICE_ENDPOINT_URL.format(page), headers=headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        return None


def process_prices_page(page):

    data_types = {
        "id": str,
        "price": float
    }

    df = pd.DataFrame.from_dict(page)
    
    return df


page = get_prices_page()
print(process_prices_page(page))