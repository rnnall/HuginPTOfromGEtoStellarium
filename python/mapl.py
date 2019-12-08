import os, sys, glob

# Creates mapping list of the image files based on Google studio extracted images 'mapl.txt'

os.chdir("mydir") # Change to source dir

mapl = open("mapl.txt","w")

for fname in glob.glob("*.jpeg"):
    mapl.write(fname + "\n")
    print("Filename: "+ fname)

mapl.close()
