import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import pandas as pd

from prices import *
from catalog import Catalog
from offers import *

def main():

    df = pd.read_csv("../bucket/catalog.csv")

    catalog = Catalog()
    print("\nReading catalog file....")
    catalog.read_catalog_csv()
    print("Finished reading catalog file!\n")

    print("Updating catalog prices....\n")
    catalog.data, error = get_product_prices(catalog.data)
    print("Done updating catalog!\n")
    if error:
        print("Error updating catalog! Job will partialy update offers.\n")
        catalog.data = catalog.data[catalog.data.price == None]

    print("Updating offers....\n")
    process_catalog_categories(catalog.data)
    print("\nDone updating offers!\n")

if __name__ == "__main__":
    main()