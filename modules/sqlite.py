import sqlite3
import os
#__file__
#sqlite3.connect(os.path.abspath(__file__+"/../../data")+"data.db")
data=sqlite3.connect(os.path.abspath(__file__+"/../../data")+"/data.db")
data.cursor()
cursor = data.cursor()