import pandas as pd

from configs import CATALOG_FILE_PATH

class Catalog:

    def __init__(self):
        self.data = None
    
    def read_catalog_csv(self):

        """
            Reads catalog csv file into a pandas DataFrame 
            and filter products by status and audience

            Parameters
            ----------
                None

            Returns
            -------
                None
        """

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

        df = pd.read_csv(CATALOG_FILE_PATH, dtype=data_types)
        # print(df.head(5))
        # print(df.dtypes)

        df['price'] = None

        df = df[(df.is_active == True) & (df.is_adult == False)]
        # print(df.head(5))

        self.data = df
