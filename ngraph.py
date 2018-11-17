#N graph

import matplotlib.pyplot as plt
import numpy as np

#Start with years

productionStartYear = int(input("Input production start year: "))
productionEndYear = int(input("Input production end year: "))
productionTimeDif = ((productionEndYear - productionStartYear) + 1 )

years = []
discharges = []
#Reach = []
#reachMax = []
dischargesC = []
#reachSum = (sum(reachMax)/(productionTimeDif - 1))

for a in range(productionStartYear,productionEndYear+1):
        year_of_Qn = int(input("What is year? "))
        years.append(year_of_Qn)
        xQn = float(input("What is discharge? "))
        discharges.append(xQn)
for x in range (years[1], productionTimeDif):
                dischargesC.append(xQn)
 #       
##ReachB =  discharges[0:productionTimeDif]
#reachMax = list(np.array(ReachG)-np.array(ReachB))

#reachNew = zip(discharges[1:]-discharges)
#dischargesC = (discharges)
#del dischargesC[0]

reachNew = [dischargesC - discharges for (dischargesC,discharges) in zip(discharges,dischargesC)]

#need to find xmedian, R, xUp and xDown     
#xmedian = (sum(discharges)/productionTimeDif)
#reachSum = (sum(reachMax)/(productionTimeDif - 1))
#print (xmedian)
print (reachNew)
#Let's get Qoil values
print 
Qoil = float(input(""))
