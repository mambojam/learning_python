# a mini-app to calculate the length of a title
text = input("enter a title:")

length = len(text)

print("Title Length:", length)

# Improved version:
text = input("enter a title:")

length = len(text)-2

print("Title Length:".capitalize(), text.title(), length) #and you write the movie title in brackets

