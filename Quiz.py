# Quiz of 5 questions

print("Select the option 1/2/3/4")
score = 0
print("\nWhat help the fish to change their direction and help them in maintaining balance in water \n1.flat fins and tails \n2.grills \n3.scales \n4.snout")
a1 = input("Your answer: ")
if a1 == "1":
    print("Your answer is correct")
    score += 1
else: 
    print("Your answer is wrong")
    
print("Which aquatic animals does not have gills? \n1.octopus \n2.lobster \n3.sea snake \n4.whale")
a2 = input("Your answer: ")
if a2 == "4":
    print("Your answer is correct")
    score += 1
else: 
    print("Your answer is wrong")
    
print("Consider the following organisms: \nCrocodile, Crow, Duck, Fish, Tortoise \nSelect the one which is different from the others. \n1.Tortoise \n2.Fish \n3.Crow \n4.Crocodile")
a3 = input("Your answer: ")
if a3 == "3":
    print("Your answer is correct")
    score += 1
else: 
    print("Your answer is wrong")
        
print("Crocodiles are mainly killed by poachers for: \n1.horns \n2.skin \n3.teeth \n4.scent")
a4 = input("Your answer: ")
if a4 == "2":
    print("Your answer is correct")
    score += 1
else: 
    print("Your answer is wrong")
    
print("____ is the most intelligent mammal on earth \n1.Hippos \n2.Dog \n3.Dolphins \n4.Deer")
a5 = input("Your answer: ")
if a5 == "3":
    print("Your answer is correct")
    score += 1
else: 
    print("Your answer is wrong")
    
print("\n Finished")
print("\n Your score is:",score)