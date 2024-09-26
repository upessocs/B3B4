
filename= "example.txt"

# Create file handle to write
file = open(filename, "r")


fileContent = file.readlines()
print(fileContent)

# save and close file
file.close()

    