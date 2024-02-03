import os

def by_numbers(s): 
    return int(''.join(char for char in s if char.isdigit()))

directory = './rendered'
files = os.listdir(directory)
files = sorted(files, key=by_numbers) 
index = 0
while index < len(files):
    filename = files[index]
    print(filename)
    index += 1
print("Has the script properly ordered it? (Y/N)")
a = input("  > ")
if a.lower() == "y":
    index = 0
    while index < len(files):
        filename = files[index]
        file = directory+"/"+filename
        os.rename(file, directory+"/"+str(index)+".png")
        print(index)
        index += 1