import requests
import pandas as pd

from configs import EMAIL, TOKEN, PRICE_ENDPOINT_URL, REQUEST_RETRIES


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
            int
                HTTP request status code
    """

    headers = {'Auth': EMAIL + ":" + TOKEN}
    
    for _ in range(REQUEST_RETRIES):
        
        try:
            response = requests.get(PRICE_ENDPOINT_URL.format(page), headers=headers)

            if response.status_code == 200:
                return response.json(), response.status_code

        except requests.exceptions.RequestException as e:
            print(e)
            return None, response.status_code 
    
    return None, response.status_code


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


def get_product_prices(catalog):

    """
        Update catalog prices

        Parameters
        ----------

            DataFrame
                Pandas dataframe with products data

        Returns
        -------
            DataFrame
                Pandas dataframe with updated products prices
            
            boll
                True if erro, False o/w
    """

    page_number = 0
    finished = False

    while not finished:

        print("Requesting page %d....\n" % page_number)   
        page_json, code = get_prices_page(page_number)
    
        if page_json:

            print("Processing page %d....\n" % page_number)   
            page_df = process_prices_page(page_json)
            page_df = page_df.set_index('id')
            catalog = catalog.set_index('id')
            catalog.update(page_df)
            catalog.reset_index(inplace=True)

            if not (True in catalog['price'].isnull()):
                page_number += 1
            else:
                finished = True
        else:
            if code == 400:
                print("Requested page %d does not exist....\n" % page_number)
                return catalog, True
            else:
                print("Error requesting page %d [%d]....\n" % (page_number, code))
                return None, True
    
    return catalog, False
