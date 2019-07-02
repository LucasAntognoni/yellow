import numpy as np
import pandas as pd

from prices import *
from catalog import Catalog

def main():

    catalog = Catalog()
    catalog.read_catalog_csv()
    print(catalog.data)
    while not catalog.updated:
        page = process_prices_page(get_prices_page(catalog.page_counter))
        # page = process_prices_page()
        catalog.data.set_index('id')
        catalog.data.update(page.set_index('id'))
        catalog.data.reset_index()
        print(catalog.data)
        catalog.page_counter += 1
        catalog.updated = not catalog.data.price.isnull().values.any()

    print(catalog.data)

if __name__ == "__main__":
    main()