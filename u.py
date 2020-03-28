def u():
    from sys import exit
    class Cancelled(Exception):
        exit("PROCESS TERMINATED -- The script was interrupted")
    print("This will OVERWRITE all files with same name in current working dir!!")
    cont = input("Would you still like to continue? y/n, case-sensitive")
    if cont == "y":
        print("removing files..")
        os.system("rm -f FileName")
        print("33% done")
        os.system("rm -f FileName")
        print("66% done")
        os.system("rm -f FileName")
        print("100% done, finished deletion")
        print("Downloading update")
        os.system("curl -o FileName https://link.to/file1")
        print("33% done")
        os.system("curl -o FileName https://link.to/file2")
        print("66% done")
        os.system("curl -o FileName https://link.to/file3")
        print("100% done, finished download")
    else:
        raise Cancelled
