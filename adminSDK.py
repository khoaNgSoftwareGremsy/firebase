import pandas as pd
import string
from numpy import isnan
from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin
from os import stat_result
import math
# from __future__ import print_function


# add credentials to app
cred = credentials.Certificate(
    "/home/khoa/Gremsy/project_pLife/firebase/firebase/gsim_json.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = pd.read_excel(r'data.xlsx', sheet_name=0)

needAtr = ['Loại hàng', 'Nhóm hàng', 'Mã hàng', 'Mã vạch',
           'Tên hàng', 'Tồn kho', 'Thương hiệu', 'Hình ảnh (url1,url2...)']

# size of data in rectangle shape
sizeOfData = data.shape
numOfEle = sizeOfData[0]

dict = {}
for i in range(0, 10):
    print("Hello Khoa")


def switch_type(variable):
    if isinstance(variable, str) == False:
        if math.isnan(variable):
            variable = str(variable)
            variable = " "
            print("new var: " + variable)
    return variable


for k in range(0, numOfEle):
    print("current : [" + str(k) + "]")
    for i in data.columns:
        for j in needAtr:
            if i == j:
                dict[j] = data.at[k, i]

                if j == 'Nhóm hàng' and dict[j].find('/') != -1:
                    dict[j] = dict[j].replace("/", "|")

    dict['Thương hiệu'] = switch_type(dict['Thương hiệu'])
    dict['Hình ảnh (url1,url2...)'] = switch_type(
        dict['Hình ảnh (url1,url2...)'])
    dict['Mã vạch'] = switch_type(dict['Mã vạch'])

    print(dict['Thương hiệu'])
    attribute = {
        u'prodName': dict['Tên hàng'],
        u'prodType': dict['Loại hàng'],
        u'prodGroup': dict['Nhóm hàng'],
        u'prodSeri': dict['Mã hàng'],
        u'prodBar': dict['Mã vạch'],
        u'prodInve': dict['storage'],
        u'prodBrand': dict['Brand'],
        u'proImg': dict['Hình ảnh (url1,url2...)'],
    }
    tempID = dict['Mã hàng']

    db.collection(u'WareHouse').document(tempID).set(attribute)
