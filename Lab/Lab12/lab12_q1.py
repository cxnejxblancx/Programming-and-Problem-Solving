# list comprehension
    # a --> [1, 2, 4, 8, 16, 32, 64, 128]
powers_of_2 = [(2 ** num) for num in range(8)]

    # b --> [0, 2, 4, 6, 8]
multiples_of_2 = [(num * 2) for num in range(5)]

    # c ==> {0: 0, 5: 25, 10: 100, 15: 225, 20: 400, 25: 625}
multiples_of_5_squared = {(num * 5): ((num * 5) ** 2) for num in range(6)}

    # d --> {5: [5, 10, 15, 20], 6: [6, 12, 18, 24], 7: [7, 14, 21, 28], 8: [8, 16, 24, 32]}
dict_of_lists = {num: [(num * i) for i in range(1, 5)] for num in range(5, 9)}

# testers
print(powers_of_2)
print(multiples_of_2)
print(multiples_of_5_squared)
print(dict_of_lists)
