import numpy as np
import pandas as pd

from prices import *
from catalog import Catalog
from offers import *

def main():

    catalog = Catalog()
    print("\nReading catalog file....")
    catalog.read_catalog_csv()
    print("Finished reading catalog file!\n")

    print("Updating catalog prices....\n")
    catalog.data, error = get_product_prices(catalog.data)
    print("Done updating catalog!\n")
    if error:
        print("Error updating catalog!\n")
        exit(1)

    print("Updating offers....\n")
    process_catalog_categories(catalog.data)
    print("Done updating offers!\n")

if __name__ == "__main__":
    main()