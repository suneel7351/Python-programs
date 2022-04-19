import os

try:
    source = "/home/suneel/Desktop/python/abc/move.txt"
    destination = "/home/suneel/Desktop/python/xyz/move.txt"

    os.rename(source, destination)

except:
    print("Error")
