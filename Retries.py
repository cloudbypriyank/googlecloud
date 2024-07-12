import requests
from time import sleep

def download_content(urls):
    contents = []
    for url in urls:
        attempt = 0
        while attempt < 3:
            try:
                response = requests.get(url)
                response.raise_for_status()
                contents.append(response.content)
                break
            except requests.exceptions.RequestException as e:
                attempt += 1
                if attempt < 3:
                    sleep(1)
                else:
                    print(f"Failed to download {url} after 3 attempts: {e}")
                    contents.append(None)
    return contents
