import requests
from sys import exit
def download(filename, url): #Source: dzone.com/articles/simple-examples-of-downloading-files-using-python
    myfile = requests.get(url)
    open(filename, 'wb').write(myfile.content)
def view(url):
    changelog = requests.get(url)
    changelog = changelog.content
version = open("version", "r") #source www.guru99.com/reading-and-writing-files-in-python.html
version = version.read()
link = "http://link.to/version" #link to file with version of program
newVer = view(link)
newVer = newVer.read()
print("Latest version: ", newVer)
print("Current version: ", version)
if newVer == version:
    print("You have the latest version.")
else:
    print("There is a new version available!")
    see = input("Do you want to view the changelog? Y/n: ")
    see.lower()
    if see == "y":
        view("link.to/changelog")
    else:
        print("OK, skipping...")
    want = input("Do you want to download the new version? (Y/n) ")
    want = want.lower()
    if want == "y":
        print("OK, downloading it")
        #TODO : add progress bar
        download(firstfilename.py, "http://url.to/file")
        download(secondfilename.py, "http://url.to/file2")
        download(thirdfilename.py, "http://url.to/file3")
        download(version, "http://url.to/version")
        print("Success !")
        print("Please restart the <ADD SCRIPT NAME HERE!>.")
        exit()
