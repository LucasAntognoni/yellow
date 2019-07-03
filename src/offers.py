import requests
import pandas as pd
from configs import EMAIL, TOKEN, CATEGORIES_GET_URL, CATEGORIES_POST_URL, REQUEST_RETRIES


def get_categories():

    """
        Get categories from Offers API

        Parameters
        ----------

        Returns
        -------
            JSON
                Categories in JSON format if successful, None o/w
            int
                HTTP request status code
    """

    headers = {'Auth': EMAIL + ":" + TOKEN}
    
    for _ in range(REQUEST_RETRIES):
        
        try:
            response = requests.get(CATEGORIES_GET_URL, headers=headers)

            if response.status_code == 200:
                return response.json(), response.status_code
            else:
                return None, response.status_code

        except requests.exceptions.RequestException as e:
            print(e)
            return None, response.status_code 
    
    return None, 500

def post_categories(category, products):

    """
        Post products to Offers API

        Parameters
        ----------
            int
                Category id

            DataFrame
                Pandas dataframe with products data

        Returns
        -------
            bool
                Categories in JSON format if successful, None o/w
            int
                HTTP request status code
    """

    json_string = products.to_json(orient = "records", force_ascii=False)
    
    headers = {'Auth': EMAIL + ":" + TOKEN}
    
    for _ in range(REQUEST_RETRIES):
        
        try:
            response = requests.post(CATEGORIES_POST_URL.format(category), headers=headers, json=json_string)
            if response.status_code == 200:
                return False, response.status_code 
        except requests.exceptions.RequestException as e:
            print(e)
            return True, response.status_code 
    
    return True, response.status_code 

def process_catalog_categories(catalog):

    """
        Process catalog products

        Parameters
        ----------

            DataFrame
                Pandas dataframe with products data

        Returns
        -------
    """

    categories = (get_categories())[0]
    
    for c in categories:

        print("Updating category: " + c['name'])
        products = catalog[(catalog.category == c['name'])]
        products = products.drop(["id", "added_at", "is_active", "category", "is_adult", "is_shippable"], axis=1)
        
        error, code = post_categories(c['id'], products)

        if error:
            print("Could not update category:" + c['name'])

