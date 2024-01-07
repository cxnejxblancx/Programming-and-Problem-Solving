# probability density function:
    # (1 / (sqrt(2 * pi)) * (e ** ((-1/2) * (x ** 2)) ) )

# import math
import math

# constants
value_x1 = float(0)
value_x2 = float(1)
value_x3 = float(-1)

# calculations
pdf1 = ((1 / (math.sqrt(2 * (math.pi))) * ((math.e) ** ((-1/2) * (value_x1 ** 2)))))
pdf2 = ((1 / (math.sqrt(2 * (math.pi))) * ((math.e) ** ((-1/2) * (value_x2 ** 2)))))
pdf3 = ((1 / (math.sqrt(2 * (math.pi))) * ((math.e) ** ((-1/2) * (value_x3 ** 2)))))

# print
print("The value of pdf at x = " + str(value_x1) + " is " + str(pdf1))
print("The value of pdf at x = " + str(value_x2) + " is " + str(pdf2))
print("The value of pdf at x = " + str(value_x3) + " is " + str(pdf3))
