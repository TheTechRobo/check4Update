from requests import get
req = get("http://www.google.com")
requ = req.text()
code = req.status_code
if code == 200:
    print("Success!")
    file = open("hello", "wb")
    file.write(requ)
else:
    print("Failure!")
