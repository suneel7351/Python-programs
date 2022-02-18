import os


try:
    if(os.path.exists("/home/suneel/Desktop/python/abc")):
        print("Folder already exist with this name")
    else:
        directory = "abc"
        parent_dir = "/home/suneel/Desktop/python/"
        fileName = "xyz.txt"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)

        filePath = os.path.join(path, fileName)
        f = open(filePath, "w")
        f.write("Hello world")
        x = open("/home/suneel/Desktop/python/abc/xyz.txt", 'r')
        print(x.read())

except:
    print("ERROR")
