import requests
from requests.exceptions import HTTPError

URLS = ["https://sky.pro/media/modul-requests-v-python/"]
for url in URLS:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        print("Success!")
        print(URLS)
print(response.content)
