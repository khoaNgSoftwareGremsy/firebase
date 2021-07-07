from __future__ import print_function
from os import stat_result
import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore
from numpy import isnan
import string
import pandas as pd

#add credentials to app 
cred = credentials.Certificate("/home/khoa/Gremsy/project_pLife/firebase/firebase/gsim-488be-firebase-adminsdk-kn2dg-33dc25f8ed.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = pd.read_excel (r'data.xlsx', sheet_name= 0)

needAtr = ['Loại hàng','Nhóm hàng(3 Cấp)','Mã hàng','Mã vạch','Tên hàng','Tồn kho','Thương hiệu','Hình ảnh (url1,url2...)']

#size of data in rectangle shape
sizeOfData = data.shape
numOfEle = sizeOfData[0]

dict = {}

for k in range(0,numOfEle):
    print("current : [" + str(k) + "]")
    for i in data.columns:
        for j in needAtr:
            if i == j:
                dict[j] = data.at[k,i]  
                if j == 'Nhóm hàng(3 Cấp)' and dict[j].find('/') != -1: 
                    dict[j] = dict[j].replace("/","|")
    attribute = {
        u'Tên hàng': dict['Tên hàng'],
        u'Mã hàng': dict['Mã hàng'],
        u'Mã vạch': dict['Mã vạch'],
        u'Tồn kho': dict['Tồn kho'],
        u'Thương hiệu':dict['Thương hiệu'],
        u'Hình ảnh': dict['Hình ảnh (url1,url2...)'],
    }

    db.collection(u'WareHouse').document(dict['Loại hàng']).collection(dict['Nhóm hàng(3 Cấp)']).document().set(attribute)

