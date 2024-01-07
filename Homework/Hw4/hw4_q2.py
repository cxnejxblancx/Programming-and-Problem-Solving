# Ingredients for 1 Batch of Mochi
    # 3 cups mochiko
    # 1.5 cups sugar
    # 2 cups cornstarch
    # 1 cup anko

# constant
GRAMS_IN_CUP = 220

# input
mochiko_grams = float(input("Enter an amount (g) of mochiko: "))
sugar_grams = float(input("Enter an amount (g) of sugar: "))
cornstarch_grams = float(input("Enter an amount (g) of cornstarch: "))
anko_grams = float(input("Enter an amount (g) of anko: "))

# conversions
mochiko_cups = mochiko_grams / GRAMS_IN_CUP
sugar_cups = sugar_grams / GRAMS_IN_CUP
cornstarch_cups = cornstarch_grams / GRAMS_IN_CUP
anko_cups = anko_grams / GRAMS_IN_CUP

# variables
batches_from_mochiko = int(mochiko_cups // 3)
batches_from_sugar = int(sugar_cups // 1.5)
batches_from_cornstarch = int(cornstarch_cups // 2)
batches_from_anko = int(anko_cups // 1)

# conditionals
if (mochiko_cups >= 3) and (sugar_cups >= 1.5) and (cornstarch_cups >= 2) and (anko_cups >= 1):
    if (batches_from_mochiko <= batches_from_sugar) and (batches_from_mochiko <= batches_from_cornstarch) and (batches_from_mochiko <= batches_from_anko):
        complete_batches = batches_from_mochiko
    elif (batches_from_sugar <= batches_from_mochiko) and (batches_from_sugar <= batches_from_cornstarch) and (batches_from_sugar <= batches_from_anko):
        complete_batches = batches_from_sugar
    elif (batches_from_cornstarch <= batches_from_mochiko) and (batches_from_cornstarch <= batches_from_sugar) and (batches_from_cornstarch <= batches_from_anko):
        complete_batches = batches_from_cornstarch
    else:
        complete_batches = int(batches_from_anko)

    print("With this amount of ingredients, you can make " + str(complete_batches) + " batch(es) of 24 mochi.")

else:
    print("With this amount of ingredients, you cannot make a batch of 24 mochi.")
