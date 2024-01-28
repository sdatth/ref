# to open a file
myfile = open("/home/datthu/Documents/deshaw/file.txt","r+")

# to read lines method 1
for line in myfile:
    # will print all the lines one by one , strip() and rstrip() function is used to remove extra empty lines
    if len(line.strip()) > 0:
        print(line.rstrip())

# to read lines method 2
content = myfile.read().splitlines()
for line in content:
    print(line)

# to read lines method 3
with open("/home/datthu/Documents/deshaw/file.txt","r+") as f:
    content = f.readlines()
    for line in content:
        print(line.rstrip())

# to write lines
myfile.write("\nHello, World. I am learning Python")    # to write a single line        
content = ["\nPython 3.x", "\nI am learning cpp too"]
myfile.writelines(content)                              # to write multiple lines

# to close file
myfile.close()
