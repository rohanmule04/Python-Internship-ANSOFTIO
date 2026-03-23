# Day 14 - File Handling in Python (Read File)
# Ansoftio Python Developer Internship

file = open("student.txt", "r")
data = file.read()
print("File Content:")
print(data)
file.close()
