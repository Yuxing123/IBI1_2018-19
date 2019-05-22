# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:01:33 2019

@author: 52935
"""
import matplotlib.pyplot as plt
import numpy as np
import os
from xml.dom.minidom import parse
import xml.dom.minidom

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
# change 
for i in range(0,5): # Run simulation for 5 times
    #pm = {}
    #DOMTree = xml.dom.minidom.parse('predator-prey.xml')
    #collection = DOMTree.documentElement
    #model_it = collection.getElementsByTagName('parameter')
    #for i in range(0,4):
        #temp = np.random.sample()
        #pm_name = model_it[i].getAttribute('id')
        #print(pm_name,':',temp)
        #pm[pm_name]=temp
        #model_it[i].setAttribute('value',str(temp))
    #filexml = open('predator-prey.xml','w')
    #DOMTree.writexml(filexml)
    #filexml.close()   
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
    plt.plot(data[0:200,1],label='Predator (b=' + str(pm['k_predator_breeds']) + ', d=' + str(pm['k_predator_dies']) + ')')
    plt.plot(data[0:200,2],label='Prey (b=' + str(pm['k_prey_breeds']) + ', d=' + str(pm['k_prey_dies']) + ')')
    plt.xlabel('time')
    plt.ylabel('population size')
    plt.legend()
    plt.title('time course')

    plt.figure(figsize=(6,4),dpi=150)
    plt.plot(data[0:200,1],data[0:200,2])
    plt.xlabel('predator population')
    plt.ylabel('prey population')
    plt.title('limit cycle')



    


