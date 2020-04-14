# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:23:04 2020

@author: himanshimehta
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
source=requests.get('https://api.covid19india.org/v2/state_district_wise.json').json()
# print(source)X
user_input=input("Enter State or District::")
lst_num=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
for i in range(len(source)):
    if(source[i]['state']==user_input):
        print("yes please enter your district")
        user=input("Enter State or District::")
        lst=source[i]['districtData']
for j in range(len(lst)):
    if(lst[j]['district']==user):
        print("In your district {} total {} confirm cases ".format(user,lst[j]['confirmed']))

       

# x=df.loc[lambda df: df['Name of State / UT']==user_input]
# print(x)
# print("Total Cases =="+x['Total Confirmed cases (Including 76 foreign Nationals)'])