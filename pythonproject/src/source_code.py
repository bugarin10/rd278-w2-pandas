"""This script does not take any modules"""
# test source code to make the python template worflow stable

import os
import pandas as pd
import sys

def descriptive_statistics(data):    
    return data.describe()



if __name__ =="__main__":
    #current_dir = os.path.dirname(os.path.abspath(__file__))
    #new_dir = current_dir + '/data'
    #sys.path.insert(0, new_dir)
    data=pd.read_csv("pythonproject/src/data/spotify.csv")
    data.describe()