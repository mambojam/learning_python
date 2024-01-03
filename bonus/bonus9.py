password = input("Enter a password that contains at least 8 characters, 1 number and 1 upper case: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True

result["uppers"] = upper

# if result == [True, True, True]:
#    print("Strong Password. Good job!")

#if all(result) == True:
if all(result.values()):
    print("Strong Password. Good job!")

else:
    print("Weak password. Try again.")


#### Or with a custom function it looks like:

password_to_check = input("Enter a new password: ")


def strength(password):

    results = {}

    if len(password) >= 8:
        results["length"] = True
    else:
        results["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    results["digits"] = digit

    upper = False
    for i in password:
        if i.isupper():
            upper = True
    results["uppers"] = upper

    if all(results.values()):
        return "Strong Password"

    else:
        return "Weak Password"


answer = strength(password_to_check)
print(answer)