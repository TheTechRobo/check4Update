from urllib2 import urlopen
def download(filename, url):
    response = urlopen(url)
    data = response.read()

    # Write data to file
    file_ = open(filename, 'w')
    file_.write(data)
    file_.close()
def view(url):
    response = urlopen(url)
    data = response.read()
    #output
version = 1.0 #update this every time, or else it will not work properly. It has to be CORRECT!
link = "https://thetechrobo.github.io/checkVersion" #link to file with version of program
newVer = view(url)
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
        view(link.to/changelog)
    else:
        print("OK, skipping...")
    want = input("Do you want to download the new version? (Y/n) ")
    want = want.lower()
    if want == "y":
        print("OK, downloading it")
        #TODO : add progress bar
        download(firstfilename.py, url.to/file)
        download(secondfilename.py, url.to/file2)
        download(thirdfilename.py, url.to/file3)
        print("Success !")
        print("Now starting the updated version...")
        #start your program here!
