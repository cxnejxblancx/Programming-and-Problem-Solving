# inputs
is_venemous = input("Is the snake venemous? ")
is_small = input("Is the snake small? ")
is_aggressive = input("Is the snake aggressive? ")

# conditionals
if is_venemous == "yes":
    if is_small == "no":
        if is_aggressive == "yes":
            print("That is a C++ Cobra. Evolved from the C Serpants many years ago. Reports show they have the weird habit of pointing at objects with their tails.")

        else:
            print("That is a C Serpent. Can be found in the sea. Has the ability to control their memory, being able to allocate parts of their brain for certain tasks and permanently delete information from their memories.")
   
    else:
        if is_aggressive == "yes":
            print("That is a Matla Mamba. Commonly used to introduce mechies to working with snakes. They often hatch plots to catch their prey and enjoys graphical images.")
        
        else:
            print("That is a Verilog Viper. Many people first see these snake around architectures. Reports claim tht they like to chew on circuit wires.")
else:
    if is_small == "no":
        if is_aggressive == "yes":
            print("That is a Assembly Anaconda. Many people hate learning about these snakes, as they look very intimidating. In the Totally Official CS1114 Snake Register, they are said to love being in low level altitudes.")
        
        else:
            print("That is a Python Python. One of the largest and most famous snakes. However, they are pretty slow, and are commonly used to introduce people to learning about snakes.")
    
    else:
        if is_aggressive == "yes":
            print("That is a Javascript Treesnake. Despite its name, they are completely different from the Java Kingsnake. They like to lay on the nodes of a tree to browse through nearby animals for their next meal.")
        
        else:
            print("That is a Java Kingsnake. Very befitting of their name, they are objectively the most sophisticated snake species. One may even say they are very classy.")
