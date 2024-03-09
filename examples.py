import os

# List all files in the current directory
path = '.'
files = os.listdir(path)
print(files)


# list recursively all files in the current directory
for root, dirs, files in os.walk(path):
    for file in files:
        print(file)

# list all files in the current directory with a specific extension
extension = '.txt'
files = [file for file in os.listdir(path) if file.endswith(extension)]
print(files)
