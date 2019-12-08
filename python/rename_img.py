import os

# This is to rename the Google Studio File so they can be importated into hugin's to match the cordianates.

os.chdir("../GEEtoHugintoStellarium/python/images/Test") # Add your path to here were the Google Image files will be located.

print("Loading List")
f = open("mapping.txt" , "r")
print("Done Loading List")
itemList= f.read().split("\n")

for each in itemList:
	try:
		each = each.strip().split(",")
	    #os.rename("Input/"+each[0], "Finished/"+each[1])
		os.rename(each[0], each[1])
		#print("/" + each[1]+ " ---- Finished/" + each[0])
	except:
		pass
