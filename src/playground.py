import requests
from google.cloud import storage


def test_requests(email, token):

    headers = {'Auth': email + ':' + token}
    data = {"name": "", "brand": "","price": 0}

    # response = requests.get('https://price-api-psel.raccoon.ag/prices', headers=headers)
    # response = requests.get('https://product-api-psel.raccoon.ag/categories', headers=headers)
    # response = requests.post('https://product-api-psel.raccoon.ag/categories/0/products', headers=headers, json=data)

    print('Status: %s' % response.status_code)
    
    for c in response.json():
        print(c)

def download_blob(bucket_name, source_blob_name, destination_file_name):
    
    storage_client = storage.Client.from_service_account_json('../authentication/account.json')

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))

# test_requests()
# download_blob("catalog-store", "catalog.sample.csv", "sample.csv")