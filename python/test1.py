import os
print("this is python, running here", os.getcwd())
#######################################################
#testing a file... need to change USERNAME
########################################################
F= open("/mnt/storage/admindi/home/USERNAME/GreatFile.txt", "wt")
F.write("This is really important\n")
F.close()

print("bye!\n")


