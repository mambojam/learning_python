date = input("Enter today's date: ")
mood = input("How do you feel out of 10 today? ")
thoughts = input("How would you describe your feelings?\n")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)
