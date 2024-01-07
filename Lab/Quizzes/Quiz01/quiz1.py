# input
age = int(input("How old are you? "))
is_accompanied = input("Are you accompanied by somebody 17-years old or more? [y/n] ")

# conditionals
if age < 17:
    if is_accompanied == "y":
        print("Allowed.")
    else:
        print("Not Allowed.")
else:
    print("Allowed.")
