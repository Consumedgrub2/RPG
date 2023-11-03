import random
import io
import os
import pathlib

test = 5
test2 = "This is the string!"

if test == 5:
    print('hi')

def helloWorld():
    print("Hello World! \nSup Mark!")
    print(str(6 + test) + " " + str(test2))

helloWorld()

someFile = open(os.getcwd() + "/test.txt", "w")
someFile.write("Hello there!")
someFile.flush()