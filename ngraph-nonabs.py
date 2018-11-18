#ngraph experimental nonabs

#Ngraph v2.0
#brought to you by yours truly @anchrone
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

productionStartYear = int(input("Input production start year: "))
productionEndYear = int(input("Input production end year: "))
productionTimeDif = ((productionEndYear - productionStartYear) + 1 )

discharges = []
dischargesOfWater = []
quantityOfWells = []
dischargeOfLiq = []

years = list(range(productionStartYear, productionEndYear+1))

#Discharge of oil
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
xDown = ((xMedian - ((3 * totalRqN)/1.128)))
dischargeUpCoef = [xUp] * len(years)
dischargeDownCoef = [xDown] * len(years)
dischargeMedianCoef =  [xMedian] * len(years)

#Discharge of water 

for currentYear in range(productionStartYear, productionEndYear+1):
    xQw = float(input("What was Qwater in year %d? " % (currentYear)))
    dischargesOfWater.append(xQw)

rQw = [abs(y-x) for x,y in zip(dischargesOfWater, dischargesOfWater[1:])]

xnewWater = np.linspace(min(years), max(years), 100)

tckWater = interpolate.splrep(years, dischargesOfWater, k =5)
y_smoothWater = interpolate.splev(xnewWater, tckWater)

plt.plot(xnewWater, y_smoothWater, label = "Q", color="blue")

totalRqW = ((sum(rQw))/productionTimeDif)
xMedianW = ((sum(dischargesOfWater))/productionTimeDif)
xUpW = (xMedianW + ((3 * totalRqW)/1.128))
xDownW = ((xMedianW - ((3 * totalRqW)/1.128)))
dischargeUpCoefW = [xUpW] * len(years)
dischargeDownCoefW = [xDownW] * len(years)
dischargeMedianCoefW =  [xMedianW] * len(years)

#Quantity of wells
for currentYear in range(productionStartYear, productionEndYear+1):
    xQNN = float(input("What was a number of wells in  %d? " % (currentYear)))
    quantityOfWells.append(xQNN)

rQNN = [round(abs(y-x)) for x,y in zip(quantityOfWells, quantityOfWells[1:])]

xnewNN = np.linspace(min(years), max(years), 100)

tckNN = interpolate.splrep(years, quantityOfWells, k =5)
y_smoothNN = interpolate.splev(xnewNN, tckNN)

plt.plot(xnewNN, y_smoothNN, label = "Q", color="blue")

totalRqNN = (abs((sum(rQNN))/productionTimeDif))
xMedianNN = (round((sum(quantityOfWells))/productionTimeDif))
xUpNN = (round(xMedianNN + ((3 * totalRqNN)/1.128)))
xDownNN = (round(xMedianNN - ((3 * totalRqNN)/1.128)))
dischargeUpCoefNN = [xUpNN] * len(years)
dischargeDownCoefNN = [xDownNN] * len(years)
dischargeMedianCoefNN =  [xMedianNN] * len(years)

#Total discharge

dischargeOfLiq = [((x + y)/365) for x,y in zip(dischargesOfWater, discharges)]
rQtotal = [(abs(y-x)) for x,y in zip(dischargeOfLiq, dischargeOfLiq[1:])]

xnewLiq = np.linspace(min(years), max(years), 100)

tckLiq = interpolate.splrep(years, dischargeOfLiq, k =5)
y_smoothLiq = interpolate.splev(xnewLiq, tckLiq)

plt.plot(xnewLiq, y_smoothLiq, label = "Q", color="blue")

totalRqLiq = (abs((sum(rQtotal))/productionTimeDif))
xMedianLiq = (((sum(dischargeOfLiq))/productionTimeDif))
xUpLiq = ((xMedianLiq + ((3 * totalRqLiq)/1.128)))
xDownLiq = ((xMedianLiq - ((3 * totalRqLiq)/1.128)))
dischargeUpCoefLiq = [xUpLiq] * len(years)
dischargeDownCoefLiq = [xDownLiq] * len(years)
dischargeMedianCoefLiq =  [xMedianLiq] * len(years)

#Results

#Results for oil
f, axarr = plt.subplots(2,2, figsize = (50,80))
qOil, = axarr[0,0].plot(xnew, y_smooth, label = "Q", color="blue")
xUpOil, = axarr[0,0].plot(years, dischargeUpCoef, label = "x UP", color = "green")
xDownOil, = axarr[0,0].plot(years, dischargeDownCoef, label = "x DOWN", color = "red")
xMedianOil, = axarr[0,0].plot(years, dischargeMedianCoef, label = "x MEDIAN", color ="yellow")

axarr[0,0].set_title('Q oil')
plt.xlabel = ("years")
plt.ylabel = ("Q oil")
axarr[0,0].legend(handles = [qOil,xUpOil,xDownOil,xMedianOil], labels=['Q oil', 'X UP', 'X DOWN', 'X MEDIAN'],loc='best')

#Results for water
qWater, = axarr[0,1].plot(xnewWater, y_smoothWater, label = "Q", color="blue")
xUpWater, = axarr[0,1].plot(years, dischargeUpCoefW, label = "x UP", color = "green")
xDownWater, = axarr[0,1].plot(years, dischargeDownCoefW, label = "x DOWN", color = "red")
xMedianWater, = axarr[0,1].plot(years, dischargeMedianCoefW, label = "x MEDIAN", color ="yellow")
axarr[0,1].set_title('Q water')
plt.xlabel = ("years")
plt.ylabel = ("Q water")
plt.legend(loc = "upper right")
axarr[0,1].legend(handles = [qWater,xUpWater,xDownWater,xMedianWater], labels=['Q water', 'X UP', 'X DOWN', 'X MEDIAN'],loc='best')


#Results for number of wells
numberQ, = axarr[1,0].plot(xnewNN, y_smoothNN, label = "Q", color="blue")
xUpNQ, = axarr[1,0].plot(years, dischargeUpCoefNN, label = "x UP", color = "green")
xDownNQ, = axarr[1,0].plot(years, dischargeDownCoefNN, label = "x DOWN", color = "red")
xMedianNQ, = axarr[1,0].plot(years, dischargeMedianCoefNN, label = "x MEDIAN", color ="yellow")
axarr[1,0].set_title('N')
plt.xlabel = ("years")
plt.ylabel = ("Number of wells")
axarr[1,0].legend(handles = [numberQ,xUpNQ,xDownNQ,xMedianNQ], labels=['N', 'X UP', 'X DOWN', 'X MEDIAN'],loc='best')


#Results for total discharge
totalQ, = axarr[1,1].plot(xnewLiq, y_smoothLiq, label = "Q", color="blue")
xUpTotal, = axarr[1,1].plot(years, dischargeUpCoefLiq, label = "x UP", color = "green")
xDownTotal, = axarr[1,1].plot(years, dischargeDownCoefLiq, label = "x DOWN", color = "red")
xMedianTotal, = axarr[1,1].plot(years, dischargeMedianCoefLiq, label = "x MEDIAN", color ="yellow")
plt.xlabel = ("years")
plt.ylabel = ("Q liquid")
axarr[1,1].set_title('Q liquid')
axarr[1,1].legend(handles = [totalQ,xUpTotal,xDownTotal,xMedianTotal], labels=['Q liquid', 'X UP', 'X DOWN', 'X MEDIAN'],loc='best')


plt.show()

"""
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
"""
