# Simple Python program to read a text file

file = open('example.txt')

# Read the contents of the file
content = file.read()

# Print the contents to the console
print(content)

# Close the file
file.close()