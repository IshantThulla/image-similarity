print("If you have new issue to be resolved by our agents, press 1")
print("If your issue has already been resolved, press 2")
print("If you want to abandon the task given by you to the agents, press 3")
total_agents = 5              
issues_already_assigned = 3
agents_available = total_agents - issues_already_assigned
while True:
	user_input = int(input())
	if user_input == 2:
		agents_available = agents_available + 1
		print("Thank you for contacting us, we are more than happy to help")
		break
	elif user_input == 3:
		agents_available = agents_available + 1
		print("Thank you for contacting us!")
		break
	elif user_input == 1:
		if agents_available >= 1:
			print("Your task has been assigned to one of our agents and he has already started working!")
			break
		else:
			print("We are sorry but there are no agents available at the moment")
			break
	else:
		print("Please enter the correct input")
		continue