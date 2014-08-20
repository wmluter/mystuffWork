#tell the user what you are asking for 
print "Type the filename again:"

#Prompt user for input after the >
file_again = raw_input("> ")

#open the file the user has asked for
txt_again = open(file_again)

# Display or print the file for the user
print txt_again.read()