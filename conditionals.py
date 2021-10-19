#set up a variable, check its value, and choose a path to follow based on the condition.

temperature = int(input("input a value between 0 and 150: "))

#compare that number with the folloing conditions:

if (temperature <=4):
    #water is frozen
    print("water's state is solid (ice)")

elif (temperature < 100):
     #water is liquid
     print("water's stateis liquid")

else:
      #water is boiling, so it's steam
      print("water is vapor")

