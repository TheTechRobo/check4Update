import requests, sys, shutil
from sys import exit
'''
Source: https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests/39217788#39217788
Thanks for using!
Please add attribution.
'''
def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
            return local_filename
def view(url):
    viewer = requests.get(url)
    viewer = viewer.raw()
    return viewer
print("Checking for updates...")
Version = open("version", "r")
onlineVersion = view("https://thetechrobo.github.io/assets/version")
if Version == onlineVersion:
    print("You are already up-to-date.")
else:
    print("You have version ", Version, "! But...there is version ", onlineVersion, " available.")
    download = input("Would you like to download it y/n? ")
    download = download.lower()
    if download == "n":
        exit("Abort.")
    else:
        print("OK, continuing...")
changelog = input("Would you like to view the changelog? Y/n: ")
changelog = changelog.lower()
if changelog == "y":
    changelog = view("https://thetechrobo.github.io")
    print(changelog.raw())
else:
    print("OK. skipping...")
print("Commencing download...")
download_file("https://hello.ca")
print("33% done.", end="\r")
download_file("https://thetechrobo.github.io")
print("66% done.", end="\r")
download_file("http://thetechrobo.byethost8.com")
print("Done download!", end="\r")
print()
