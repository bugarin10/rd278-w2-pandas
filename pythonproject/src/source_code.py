"""This script does not take any modules"""
# test source code to make the python template worflow stable

import os
import pandas as pd
import sys

def descriptive_statistics(data):    
    return data.describe()



if __name__ =="__main__":
    data=pd.read_csv("pythonproject/src/data/spotify-2023.csv",encoding="ISO-8859-1")
    print(descriptive_statistics(data))
    print(type(descriptive_statistics(data)))
    