import os
print(dir(os))

#prints directory contents
print(os.system("dir"))

os.getcwd()  # current working directory
os.chdir("C:\\Niraj") # change working directory
os.listdir("C:\\")  

os.mkdir("C:\\Niraj\\ospython") # creates directory
os.rmdir("C:\\Niraj\\ospython") #removes directory

os.makedirs("C:\\Niraj\ospython\\niraj\\abc") # makes directory recursively
os.environ  # lists environment variables
os.environ.get("ALLUSERSPROFILE") # for a specific variable


os.path.exists("C:\\Niraj")  #returns boolean values True or false if the directory exists
os.path.isfile("C:\\Niraj") # checks the path is file 
 
os.path.basename("C:\\Niraj") # returns Niraj
os.path.join("abc","def") # concatenates abc and def and automatically adds delimiter \\ or / based on operating system

list(os.walk("C:\\Niraj")) # gives a directory tree and all the files underneath
for dirname, dirpath, filename in os.walk("C:\\Niraj"):
    print(dirname)
    print(filename)

