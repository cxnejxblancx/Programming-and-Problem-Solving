# import
from math import sin

# input
frequency = float(input("Enter a value for the frequency, w: "))
duration = float(input("Enter a value for the duration of the sound wave, T: "))

# calculations
amp_spectrum = round(((2 * sin(frequency * duration)) / frequency), 3)

# final print
print("The amplitude spectrum of this Fourier transform is: " + str(amp_spectrum))
