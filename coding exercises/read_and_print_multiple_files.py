filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)


#file = open("a.txt", 'r')
#content = file.readlines()
#file.close()

#list.append(f"{content}")

#file = open("b.txt", 'r')
#content = file.readlines()
#file.close()

#list.append(f"{content}")

#file = open("c.txt", 'r')
#content = file.readlines()
#file.close()

#list.append(f"{content}")

print(list)