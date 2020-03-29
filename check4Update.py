from u import u #To launch update script
from urllib.request import urlopen #To read URL
import sys #To exit
v = "1.0" #Variable of using version

class DownErr(Exception):
    print("ERROR DOWNLOADING WEBSITE -- CHECK INTERNET CONNECTION")
    print("To debug, prefix line 18 with a #")
    sys.exit()
class QuestionQuestionQuestionableError(Exception):
    print("Random error. If it is known the error is shown above")
    sys.exit()
link = "https://thetechrobo.github.io/checkVersion" #URL to download
try:
    f = urlopen(link) #Download URL
    nV = f.read() #Read the downloaded URL
except: #If error occurs
    raise DownErr
    unsu = True
finally: #whether error occurs or not
    if unsu == True:
        print("Process failed")
        raise QuestionQuestionQuestionableError
    else:
        print("Process success!")
if nV != v:
    print("Latest version:", nV)
    print("You are utilising version ", v)
    rN = input("Show release notes???  y/n, case sensitive")
    if rN.lower() in ['y', 'yes']:
        link = "url.to/file" #URL to download
        try:
            f = urlopen(link) #Download URL
            nV = f.read() #Read the downloaded URL
        except: #If error occurs
            raise DownErr
            unsu = True
        finally: #whether error occurs or not
            if unsu == True:
                print("Process failed")
                raise QuestionQuestionQuestionableError
            else:
                print("Process success!")
    yN = input("Download newest version?? y/n, case-sensitive")
    if yN.lower() in ['y', 'yes']:
        u()
    else:
        print("You should definitley download it ASAP :)")
elif nV == v:
    print("You have the Latest Version ;)")
