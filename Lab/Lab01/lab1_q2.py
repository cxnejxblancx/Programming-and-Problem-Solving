# Metric measures for 10 SCONES
    # 75 g salted butter
    # 350 g flour
    # 150 ml milk

# Conversion Factors:
    # 75 grams butter = 1/3 cup of butter
        # 225 grams in 1 cup of butter
    # 150 gram flour = 1 cup flour
    # 100 mL milk = 1/2 cup milk
        # 200 mL in 1 cup milk

# input
num_scones = int(input("Enter the number of scones you want to make: "))

# conversions
conversion_factor = (num_scones / 10)
    # butter
butter_grams = conversion_factor * 75
butter_cups = float(butter_grams / 225)
    # flour
flour_grams = conversion_factor * 350
flour_cups = float(flour_grams / 150)
    # milk
milk_ml = conversion_factor * 150
milk_cups = float(milk_ml / 200)

# print
print("To make " +  str(num_scones) + " scones use " + str(butter_cups) + " cups butter, " + str(flour_cups) + " cups flour, and " + str(milk_cups) + " cups milk")
