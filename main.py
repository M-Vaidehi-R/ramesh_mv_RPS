from random import randint

	#save the player as a variable called player
	#the value of player will be one of three choices to type (input)

	#add player and computer lives

	#player will be the weapon the player choses via input
	# Boolean values are true-false values - u can use these to check state 
	# and then make programming choices based on their value


 
playerlives=2
computerlives=2 


	#an array is just a container. It holds multiple values in a 0-based index
	# you can store anything in an array and retrieve it later. Arrays have square bracket notations


#create an infinite loop (for  now) so that we can keep playing


player = input("Choose rock, paper or scissors: ");
choices = ["rock", "paper", "scissors"]	        
computer = choices[randint(0,2)]
print("player chose:" + player)
print("computer chose: " + computer)

if(computer==player):
				print("tie!..try again")

elif(player =="rock"):
  if(computer=="paper"):
					print("you lose!")
					playerlives = playerlives-1   
					
  else:
				    print("you win!!!")
				    computerlives = computerlives-1
				


elif(player =="paper"):
  if(computer =="scissors"):
					print("you lose!")
					playerlives = playerlives-1   
					
  else:
				     print("you win!!!")
				     computerlives = computerlives-1
				        
				      
				
			   	

			 
elif(player =="scissors"):
  if(computer=="rock"):
					print("you lose!")
					playerlives = playerlives-1  
					
  else:
				    print("you win!!!")
				    computerlives = computerlives-1
			           
			        
print("playerlives:" + str(playerlives)) 
print("computerlives:" + str(computerlives))

 
	 
       