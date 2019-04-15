# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:51:20 2019

@author: 52935
"""




from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
def Child(id,resultSet):
    for t in terms:
        parents = t.getElementsByTagName('is_a')
        geneid = t.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                resultSet.add(geneid)
                Child(geneid,resultSet)


#------main--------------
DOMTree = xml.dom.minidom.parse(r'C:\Users\52935\Desktop\ibi\IBI1_2018-19\Practical8/go_obo.xml')
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
dic = {'id':[],'name':[],'defination':[],'childNodes':[]}
for i in terms:
    text = i.getElementsByTagName('defstr')[0]
    t = text.childNodes[0].data 
    if 'autophagosome' in t :
        child = i.getElementsByTagName('is_a')
        ids = i.getElementsByTagName('id')[0]
        name = i.getElementsByTagName('name')[0]
        id = ids.childNodes[0].data
        p = name.childNodes[0].data
        resultSet = set()
        Child(id,resultSet)
        dic['id'].append(id)
        dic['name'].append(p)
        dic['defination'].append(t)
        dic['childNodes'].append(len(resultSet))
        
dt = pd.DataFrame(dic)
dt.to_excel(r'C:\Users\52935\Desktop\ibi\IBI1_2018-19\Practical8/autophagosome.xlsx',sheet_name='sheet1')        
    
    
        
    