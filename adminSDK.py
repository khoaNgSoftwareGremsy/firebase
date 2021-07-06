from __future__ import print_function
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from numpy import isnan
import string
import pandas as pd

data = pd.read_excel (r'data.xlsx', sheet_name= 0)
# columns = data.columns
needAtr = ['Loại hàng','Nhóm hàng(3 Cấp)','Mã hàng','Mã vạch','Tên hàng','Thương hiệu','Tồn kho','Hình ảnh (url1,url2...)']

dict = {}


for i in data.columns:
    for j in needAtr:
        if i == j:
            if data.at[3,i] == ' ': 
                dict[j] = 'a'
            else:
                dict[j] = data.at[3,i] 


print(dict)



# df = pd.DataFrame(data,header = 1, usecols = "A:O",nrow = 1)
# print(dict)   


# while()

# data = {
#     u'name' : u'Los Angeles',
#     u'state' : u'CA',
#     u'country' : u'USA'
# }
# def auth_with_admin_privileges():
#     #fetch the service acccount key JSON file content
#     cred = credentials.Certificate('gsim-488be-firebase-adminsdk-kn2dg-33dc25f8ed.json')

#     #initialize app with a service account , granting admin privileges
#     firebase_admin.initialize_app(cred)
#     # As an admin, the app has access to read and write all data, regradless of Security Rules
#     db = firestore.client()
    


