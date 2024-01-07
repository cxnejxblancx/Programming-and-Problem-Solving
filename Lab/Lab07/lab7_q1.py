#1
name = "Grace Hopper"

print(name[-1])

for char in range(len(name)):
    if char == 1:
        print(name[char])

print(name[:5])


# SEPARATE
print()

#2
name2 = "alan turing"

print(name2[:4].capitalize())
print(name2[5:].capitalize())


# SEPARATE
print()

#3
S = "Computer Science"

print(S[:8:2] + S[8::2])
print(S[:4] + S[8:12])


# SEPARATE
print()

#4
place = "Bletchley Park, England"

print(place[16:19] + place[19:])
print(place[-15:-17:-1] + place[-17::-1])
