# Day 13 - File Handling in Python (Write File)
# Ansoftio Python Developer Internship

file = open("student.txt", "w")
file.write("Name: Rahul\n")
file.write("Age: 22\n")
file.write("City: Pune\n")
file.write("Course: MCA\n")
file.close()

print("File 'student.txt' created and data written successfully!")
