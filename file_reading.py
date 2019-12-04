file = open("message.txt")
content = file.read()
print(content)
file.close()

file = open("message.txt")
content = file.readlines()
print(content)
file.close()

file = open("message.txt")
content = file.readline()
print(content)
file.close()

file = open("message.txt")
for line in file:
    print(line)
file.close()


