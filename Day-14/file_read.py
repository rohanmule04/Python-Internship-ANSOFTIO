# Day 14 - File Handling in Python (Read File)
# Ansoftio Python Developer Internship

file = open(r"D:/Python_internship/Python-Internship-ANSOFTIO/Day-13/student.txt", "r")
data = file.read()
print("File Content:")
print(data)
file.close()
