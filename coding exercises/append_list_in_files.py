new_member = input("Enter a new member name: ") + "\n"

file = open("members.txt.", "r")
members = file.readlines()
file.close()

members.append(new_member)

file = open("../members.txt", "w")
file.writelines(members)
file.close()