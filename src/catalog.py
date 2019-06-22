import os
import pandas as pd

class Catalog:

    def __init__(self):
        self.catalog = None
        self.data = None

    def get_catalog(self):
        pass

    def process_catalog(self):

        data_types = {
            "id": str,
            "name": str,
            "brand": str,
            "added_at": str,
            "is_active": bool,
            "category": str,
            "is_adult": bool,
            "is_shippable": bool
        }

        df = pd.read_csv('../bucket/catalog.sample.csv')
        # print(df.head(5))
        # print(df.dtypes)

        df = df[(df.is_active == True) & (df.is_adult == False)]
        # print(df.head(5))

        df = df.groupby('category')
        # print(df.head(5))

catalog  = Catalog()
catalog.process_catalog()