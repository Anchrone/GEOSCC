#Ngraph v1.8
#brought to you by yours truly @anchrone
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

productionStartYear = int(input("Input production start year: "))
productionEndYear = int(input("Input production end year: "))
productionTimeDif = ((productionEndYear - productionStartYear) + 1 )

discharges = []

years = list(range(productionStartYear, productionEndYear+1))


for currentYear in range(productionStartYear, productionEndYear+1):
    xQn = float(input("What was Qoil in year %d? " % (currentYear)))
    discharges.append(xQn)

rQn = [abs(y-x) for x,y in zip(discharges, discharges[1:])]

xnew = np.linspace(min(years), max(years), 100)

tck = interpolate.splrep(years, discharges, k =5)
y_smooth = interpolate.splev(xnew, tck)

plt.plot(xnew, y_smooth, label = "Q", color="blue")

totalRqN = ((sum(rQn))/productionTimeDif)
xMedian = ((sum(discharges))/productionTimeDif)
xUp = (xMedian + ((3 * totalRqN)/1.128))
xDown = (abs(xMedian - ((3 * totalRqN)/1.128)))
dischargeUpCoef = [xUp] * len(years)
dischargeDownCoef = [xDown] * len(years)
dischargeMedianCoef =  [xMedian] * len(years)
plt.plot(years, dischargeUpCoef, label = "x UP", color = "green")
plt.plot(years, dischargeDownCoef, label = "x DOWN", color = "red")
plt.plot(years, dischargeMedianCoef, label = "x MEDIAN", color ="yellow")
plt.title("Q of oil graph")
plt.legend(loc = "best")
plt.xlabel("years")
plt.ylabel("Q")
plt.show()

msgTwo = input("Press ENTER to continue: ")
quit()
