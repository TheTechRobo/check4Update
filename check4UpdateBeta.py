import requests
def down(url, filename):
    response = requests.get(url, stream=True)
    with open(filename, "wb") as handle:
        handle.write(data)
