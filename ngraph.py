#Ngraph v.1.5

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
        
        
rQn = [abs(y-x) for x,y in zip(discharges, discharges[1:])]

totalRqN = ((sum(rQn))/productionTimeDif)
xMedian = ((sum(discharges))/productionTimeDif)
xUp = (xMedian + ((3 * totalRqN)/1.128))
xDown = (abs(xMedian - ((3 * totalRqN)/1.128)))
dischargeUpCoef = [xUp] * len(years)
dischargeDownCoef = [xDown] * len(years)
dischargeMedianCoef =  [xMedian] * len(years)
plt.plot(years, discharges, label ="Q", color = "blue")
plt.plot(years, dischargeUpCoef, label = "x UP", color = "green")
plt.plot(years, dischargeDownCoef, label = "x DOWN", color = "red")
plt.plot(years, dischargeMedianCoef, label = "x MEDIAN", color ="yellow")
plt.title("Q of oil graph")
plt.legend()
plt.show()

#for x in range (years[1], productionTimeDif):
 #               dischargesC.append(xQn)
 #       



##ReachB =  discharges[0:productionTimeDif]
#reachMax = list(np.array(ReachG)-np.array(ReachB))

#reachNew = zip(discharges[1:]-discharges)
#dischargesC = (discharges)
#del dischargesC[0]


#need to find xmedian, R, xUp and xDown     
#xmedian = (sum(discharges)/productionTimeDif)
#reachSum = (sum(reachMax)/(productionTimeDif - 1))
#print (xmedian)
msgOne = input("Press ENTER to look at your values: ")

print (totalRqN,xMedian,xUp,xDown)
msgTwo = input("Press ENTER to continue: ")
quit()
#Let's get Qoil values
Qoil = float(input(""))
