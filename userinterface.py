import mmt

print("Welcome to PyHoliday")
init = input("Enter your start location : ")
n = int(input("Enter number of destinations you will be going to : "))
b = input("Will this be a return journey? Enter Y for yes and N for no : ")
numad = input("Number of adults travelling : ")
numch = input("Number of children travelling : ")
numin = input("Number of infants travelling : ")

destlist = [init]
datelist = []

i=1
while i <= n :
	destlist.append(input("Enter next destination : "))
	datelist.append(input("Enter date of travel : "))
	i = i +1

datelist.append(input("Enter date of end of tour : "))


	
i=1 
while i <= n :
	
	mmt.planTrip( destlist[i-1] , destlist[i] , datelist[i-1] , datelist[i] , numad , numch , numin )
	i = i+1
	
if b == "Y" :
	mmt.planTravel( destlist[n] , init , datelist[n] , numad , numch , numin )
		



