import sqlite3
import os
import modules.data as m_data

#__file__
#sqlite3.connect(os.path.abspath(__file__+"/../../data")+"data.db")
data= sqlite3.connect(os.path.abspath(__file__+"/../../data")+"/data.db")
# product_data = sqlite3.connect(os.path.abspath(__file__+"/../../product_data")+"/product_data.db")
# data.cursor()
cursor = data.cursor()
# product_cursor = product_data.cursor()
cursor.execute(f"CREATE TABLE IF NOT EXISTS List_products (INTEGER PRIMARY KEY,id)")

<<<<<<< HEAD
def add_product(name,description,path,message):
=======
def add_product(name,description,path,message=None):
>>>>>>> c03835e43f11fb84ba0ac562002598c9ee7e2cf1
    
    cursor.execute(f"CREATE TABLE IF NOT EXISTS Product_{name} (INTEGER PRIMARY KEY,id)")
    add_column("description", type_column="TEXT",name_table=f"Product_{name}")
    add_column("path", type_column="TEXT",name_table=f"Product_{name}")
    count = get_value("count_product","list_products")
    if count == []:
        count = 0
    else:
        count = int(count[-1][-1])+1
    # add_column(f"product_{m_data.count}", type_column="TEXT",name_table=f"List_products")
    set_value(columns=("product","count_product"),values=[name,count],name_table="List_products")
    set_value(columns=("description","path"),values=[description,path],name_table=f"Product_{name}")
    # m_data.count +=1 
    data.commit()
# ё
def add_column(name_column,type_column,name_table="Users"):
    try:
        cursor.execute(f"ALTER TABLE {name_table} ADD COLUMN {name_column} {type_column}")
        return "execute"
    except:
        print("Error column")
        return "Error"
def delete_column(name_column):
    try:
        cursor.execute(f"ALTER TABLE Users DROP COLUMN {name_column}")
    except:
        print("Error column")
# def create_table()
# [] list
# 0.0 float
# 0 int
# '' str
# True bool
# () tuple
# {} dict
def get_value(column= "*",name_table="AdminPassword"):
    cursor.execute(f"SELECT {column} FROM {name_table}")
    # try:

    #     return cursor.fetchall()[0][0]
    # except:
    return cursor.fetchall()
def set_value(columns=("name",'123'),values=[],name_table="Users"):

    text=""
    for column in range(len(columns)-1):
        text+="?,"
    text+="?"
    cursor.execute(f"INSERT INTO {name_table} {columns} VALUES ({text})",values)
add_column("product", type_column="TEXT",name_table=f"List_products")
add_column("count_product", type_column="INTEGER",name_table=f"List_products")
try:

    m_data.count=get_value(column= "count_product",name_table="List_products")
    print(m_data.count)
    if type(m_data.count)!=type(1):
        m_data.count = m_data.count[0]
except:
    m_data.count=0

    # set_value
# if add_column("count_product", type_column="INTEGER",name_table=f"List_products")=="Error":
#     m_data.count=get_value(column= "count_product",name_table="list_products")

# add_product("burger","bugrer","buburger")
# get_value(column="product_1",name_table="List_products")
print(get_value(column="count_product",name_table="List_products"),132)