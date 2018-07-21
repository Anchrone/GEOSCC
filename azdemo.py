#azerbaijan demographics script v0.1
#1960- 3815.7
#1970- 5117.1 
#1980- 6114.3
#1990- 7131.9
#2000- 8032.8
#2010- 9000.0

year_1960 = 3815.7
year_1970 = 5117.1
year_1980 = 6114.3
year_1990 = 7131.9
year_2000 = 8032.8
year_2010 = 9000.0

decade_change_60_70 = year_1970 / year_1960
decade_change_70_80 = year_1980 / year_1970
decade_change_80_90 = year_1990 / year_1980
decade_change_90_00 = year_2000 / year_1990
decade_change_00_10 = year_2010 / year_2000

print "60-70: %.3f, 70-80: %.3f, 80-90: %.3f, 90-00: %.3f, 00-10: %.3f" % (decade_change_60_70, decade_change_70_80, decade_change_80_90, decade_change_90_00, decade_change_00_10)

decade_median_change = (decade_change_60_70 + decade_change_70_80 + decade_change_80_90 + decade_change_90_00 + decade_change_00_10 ) / 5
annual_median_change = decade_median_change * 0.01
print "Decade median change in population is x%f" % decade_median_change
print "Annual median change in populatin  is x%f" % annual_median_change

print "Input desired year to learn Azerbaijan's estimated population:"
desired_year = int(raw_input())

estimated_population = ((desired_year - 2010) * (annual_median_change * year_2010)) + year_2010
print "In year %d the population of Azerbaijan is estimated to be %.3f" % (desired_year, estimated_population)
