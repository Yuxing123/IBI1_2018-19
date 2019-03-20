DNA = input("give me a sequence of DNA : ")
DNA = list(DNA)
myDict = {}
for i in DNA:
    if i in myDict:
        myDict[i] += 1
    else:
        myDict[i] = 1
print(myDict)

import matplotlib.pyplot as plt
labels='A','T','G','C'
sizes=myDict['A'],myDict['T'],myDict['C'],myDict['G']
colors='lightgreen','gold','lightskyblue','lightcoral'
explode=0.1,0.1,0.1,0.1
plt.pie(sizes,explode=explode,labels=labels,
        colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.axis('equal')
plt.show()
