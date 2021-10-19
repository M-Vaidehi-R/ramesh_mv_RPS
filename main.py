from random import randint

#save the player as a variable called player
#the value of player will be one of three choices to type (input)

#add player and computer lives

playerlives=5
computerlives=5 

player = input("Choose rock, paper or scissors: ");

print("player chose: " + player)

#an array is just a container. It holds multiple values in a 0-based index
# you can store anything in an array and retrieve it later. Arrays have square bracket notations
choices = ["rock", "paper", "scissors"]



computer = choices[randint(0,2)]
print("computer chose: " + computer)

if(computer==player):
	print("tie!..try again")

if(player =="rock"):
	if(computer=="paper"):
		print("you lose!")
		 playerlives=playerlives-1
		
	else:
	    print("you win!!!")
	    computerlives=computerlives-1
	    
	    
	


elif(player =="paper"):
	if(computer =="scissors"):
		print("you lose!")
		 playerlives=playerlives-1
		
	else:
	     print("you win!!!")
	     computerlives =computerlives-1
	      
	
   	

 
elif(player =="scissors"):
	if(computer=="rock"):
		print("you lose!")
		 playerlives=playerlives-1
		
	else:
	    print("you win!!!")
         computerlives=computerlives-1
        





print("playerlives:" + str(playerlives)) 
print("playerlives:" + str(computerlives))
       
	