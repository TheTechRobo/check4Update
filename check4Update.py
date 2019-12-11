v = "1.0"
from urllib.request import urlopen

link = "https://thetechrobo.github.io/checkVersion"
f = urlopen(link)
nV = f.read()
print("The new version is ", nV)
if nV != v:
    print("You are utilising version ", v)
elif nv == v:
    print("You have the Latest Version")