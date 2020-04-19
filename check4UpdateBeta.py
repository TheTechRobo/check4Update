import requests
def down(url, filename):
    downloadedFile = requests.get(url, stream=True)
    downloadedFile = downloadedFile.get()
    with open(filename, "wb") as handle:
        handle.write(response)
down("https://hello.ca", "hello.html")
