f = open("file.txt", "r")
print(f.read())
print(f.read(2))
print(f.readline())

for line in f:
  print(line)

f.close()


f = open("file.txt", "w")
f.write("Line 4")
f.close()

f = open("file.txt", "r")
print(f.read())
f.close()


# File open modes:
# "r" - Read - will open an existing file for reading, returns an error if the file exists.

# "x" - Create - will create a file, returns an error if the file exists.

# "a" - Append - will create a file if the specified file does not exist.

# "w" - Write - will create a file if the specified file does not exist.