# fileSearch
import os

def searchdirs(folder, string):
    for file in os.listdir(folder):
        f = os.path.join(folder, file)
        if(f.find(string, 0)>=0):
            print(f)
        if os.path.isdir(f):
            searchdirs(f,string)
            
start = "./tree"
name = "python"
searchdirs(start, name)

