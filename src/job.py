from prices import *
from catalog import Catalog


def main():

    catalog = Catalog()
    catalog.read_catalog_csv()
    # print(catalog.catalog)

    page = process_prices_page(get_prices_page(1))
    # print(page)

    df = pd.merge(page, catalog.catalog, on='id')

    print(df[df.price.notnull()])

if __name__ == "__main__":
    main()