
#process the Command line for arguments
from sys import argv

#retrieve the file name for the command line
script, filename = argv

#open the file
txt = open(filename)

# display the file for the command line
print "Here's your file %r:" % filename

#Display or print the file for the user
print txt.read()

#tell the user what you are asking for 
print "Type the filename again:"

#Prompt user for input after the >
file_again = raw_input("> ")

#open the file the user has asked for
txt_again = open(file_again)

# Display or print the file for the user
print txt_again.read()

# x=close(file_again)
