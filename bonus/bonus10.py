while True:
    try:
        width = float(input("enter the width: "))
        length = float(input("enter the length "))

        area = width * length
        print("area is: ", area, "m")
        break

    except ValueError:
        print("please enter a number")
