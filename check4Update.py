from subprocess import Popen #To launch update script
from urllib.request import urlopen #To read URL
v = "1.0" #Variable of using version

link = "https://thetechrobo.github.io/checkVersion" #URL to download
try:
    f = urlopen(link) #Download URL
    nV = f.read() #Read the downloaded URL
except: #If error occurs
    print("An error occured in downloading website..")
    unsu = True
finally: #whether error occurs or not
    if unsu == True
        print("Process failed")
    else:
        print("Process success!")
if nV != v:
    print("Latest version:", nV)
    print("You are utilising version ", v)
    yN = input("Download newest version?? y/n, case-sensitive")
    if yN == "y":
        
elif nV == v:
    print("You have the Latest Version ;)")
