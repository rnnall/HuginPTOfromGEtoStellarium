import os, sys

# Joins the master image names 'mapl.txt' with 'master.txt' into a mapping list to be used with 'rename_files.py' to convert the names of the files from the Google Earth Studio output zip

os.chdir("mydir")

f1_in = open("mapl.txt")
f2_in = open("master.txt")
output = open("mapping.txt", "w")
for left, right in zip(f1_in, f2_in):
    #use rstrip to remove the newline character from the left string
    output.write(left.rstrip() + "," + right)
    print("CHANGE FROM " + '"' + left.rstrip('\n') + '"' + " TO " + '"' + right.rstrip('\n')+ '"')

f1_in.close()
f2_in.close()
output.close()
