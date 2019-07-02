import requests
import pandas as pd

from configs import EMAIL, TOKEN, PRICE_ENDPOINT_URL


def get_prices_page(page):
    
    """
        Get products prices page from Price API

        Parameters
        ----------
            int
                Page number

        Returns
        -------
            JSON
                Page content in JSON format if successful, None o/w
    """

    headers = {'Auth': EMAIL + ":" + TOKEN}
    
    try:
        response = requests.get(PRICE_ENDPOINT_URL.format(page), headers=headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        return None


def process_prices_page(page):

    """
        Loads page JSON to a pandas DataFrame

        Parameters
        ----------
            int
                Page number
                    default: 0

        Returns
        -------
            DataFrame
                Page pandas DataFrame
    """

    data_types = {
        "product_id": str,
        "price": float
    }

    df = pd.DataFrame.from_dict(page)
    df.columns = ["price", "id"]
    
    return df
