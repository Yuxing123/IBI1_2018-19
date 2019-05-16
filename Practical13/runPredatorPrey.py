# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:01:33 2019

@author: 52935
"""
import matplotlib.pyplot as plt
import numpy as np
import os
os.chdir(r'C:\Users\52935\Desktop\ibi\IBI1_2018-19\Practical13/')
# xml_to_cps
def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()
# use like black box
xml_to_cps()
os.system('CopasiSE.exe predator-prey.cps')
data=[]
with open(r'modelResults.csv') as modelResults:
    lines=modelResults.readlines()
    for i in lines:
        i=i.replace('\n','') 
        if i=='Time,[A],[B]':
            variable=i.split(',')
        else:
            data.append(i.split(','))
data = np.array(data)
data = data.astype(np.float)
plt.figure(figsize=(6,4),dpi=150)
plt.plot(data[0:200,1],label='predator(b=0.02, d=0.4)')
plt.plot(data[0:200,2],label='prey(b=0.1, d=0.02)')
plt.xlabel('time')
plt.ylabel('population size')
plt.legend()
plt.title('time course')

plt.figure(figsize=(6,4),dpi=150)
plt.plot(data[0:200,1],data[0:200,2])
plt.xlabel('predator population')
plt.ylabel('prey population')
plt.title('limit cycle')

# not complete code
"""
DOMTree = xml.dom.minidom.parse(r'C:\Users\52935\Desktop\ibi\IBI1_2018-19\Practical13/predator-prey.xml')

    