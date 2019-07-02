import os
import requests
from google.cloud import storage
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../authentication/account.json'

def test_requests(page):

    headers = {'Auth': "antognoni.lucas@gmail.com:264a8d30c80b435099d42d2f8705ccaf"}
#     data = {"name": "", "brand": "","price": 0}

    response = requests.get('https://price-api-psel.raccoon.ag/prices?page={}'.format(page), headers=headers)
#     response = requests.get('https://product-api-psel.raccoon.ag/categories', headers=headers)
    # response = requests.post('https://product-api-psel.raccoon.ag/categories/0/products', headers=headers, json=data)

    print('Status: %s' % response.status_code)
    
    for c in response.json():
        print(c)

i = 0
test_requests(i)

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    print('ok 1')
    storage_client = storage.Client()
    print('ok 2')
    bucket = storage_client.get_bucket(bucket_name)
    print('ok 3')
    blob = bucket.blob(source_blob_name)
    print('ok 4')

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))

# download_blob("catalog-store", "catalog.sample.csv", "sample.csv")