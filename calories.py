 # user is provided options and gets to choose what they would eat
print("Choose the prefered meals for Breakfast: ")
breakfast = input("A. Oatmeal (158 calories)\nB. 3 Pancakes(164 calories)\nC. Honey nut cheerios with whole milk (222 calories)\n")
print("Choose the prefered meals for Lunch: ")
lunch = input("A. Chicken Caesar Salad (470 Calories)\nB. Ham and turkey sub(505 calories)\nC. Mcdonalds 10 piece Chicken McNugget meal(950 calories\n")
print(" Choose the prefered meals for Dinner: ")
dinner = input("A. Shrimp Alfredo (1148 Calories)\nB. Salmon with brown rice and veggies (502 calories)\nC. Grilled chicken w. Rice and beans (428 Calories)\n")

#if then statements to ad the sums 
if breakfast == "A" and lunch =="A" and dinner =="A":
	print("Sorry, your total calories is 1,776. You won't be able to lose 1lb.")
elif breakfast == "A" and lunch == "B" and dinner == "A":
	print("Sorry, your total calories is 1,811. You won't be able to lose 1lb.")
elif breakfast == "A" and lunch == "B" and dinner == "B":
	print("Congrats, your total calories is 1,165. You can lose approximately 1lb !")
elif breakfast == "A" and lunch == "B" and dinner == "C":
	print("Congrats, your total calories is 1,091. You can lose approximately 1lb !")
elif breakfast == "A" and lunch == "A" and dinner == "B":
	print("Congrats, your total calories is 1,130. You can lose approximately 1lb !")
elif breakfast == "A" and lunch == "A" and dinner == "C":
	print("Congrats, your total calories is 1,056. You can lose approximately 1lb !")
elif breakfast == "A" and lunch == "C" and dinner == "A":
	print("Sorry, your total calories is 2,258. You won't be able to lose 1lb.")
elif breakfast == "A" and lunch == "C" and dinner == "B":
	print("Sorry, your total calories is 1,610. You won't be able to lose 1lb.")
elif breakfast == "A" and lunch == "C" and dinner == "C":
	print("Sorry, your total calories is 1,536. You won't be able to lose 1lb.")
elif breakfast == "B" and lunch == "A" and dinner == "A":
	print("Sorry, your total calories is 1811. You won't be able to lose 1lb.")
elif breakfast == "B" and lunch == "B" and dinner == "A":
	print("Sorry, your total calories is 1782. You won't be able to lose 1lb.")
elif breakfast == "B" and lunch == "B" and dinner == "B":
	print("Congrats, your total calories is 1,171. You can lose approximately 1lb !")
elif breakfast == "B" and lunch == "B" and dinner == "C":
	print("Congrats, your total calories is 1,097. You can lose approximately 1lb !")
elif breakfast == "B" and lunch == "A" and dinner == "B":
	print("Congrats, your total calories is 1,136. You can lose approximately 1lb !")
elif breakfast == "B" and lunch == "A" and dinner == "C":
	print("Congrats, your total calories is 898. You can lose approximately 1lb !")
elif breakfast == "B" and lunch == "C" and dinner == "A":
	print("Congrats, your total calories is 1,062. You can lose approximately 1lb !")
elif breakfast == "B" and lunch == "C" and dinner == "B":
	print("Sorry, your total calories is 1,616. You won't be able to lose 1lb.")
elif breakfast == "B" and lunch == "C" and dinner == "C":
	print("Sorry, your total calories is 1,542. You won't be able to lose 1lb.")
elif breakfast == "C" and lunch == "A" and dinner == "A":
	print("Sorry, your total calories is 1840. You won't be able to lose 1lb.")
elif breakfast == "C" and lunch == "A" and dinner == "B":
	print("Congrats, your total calories is 1,194. You can lose approximately 1lb !")
elif breakfast == "C" and lunch == "A" and dinner == "C":
	print("Congrats, your total calories is 1,120. You can lose approximately 1lb !")
elif breakfast == "C" and lunch == "B" and dinner == "A":
	print("Sorry, your total calories is 1,875. You won't be able to lose 1lb.")
elif breakfast == "C" and lunch == "B" and dinner == "B":
	print("Congrats, your total calories is 1,229. You can lose approximately 1lb !")
elif breakfast == "C" and lunch == "B" and dinner == "C":
	print("Congrats, your total calories is 1,155. You can lose approximately 1lb !")
elif breakfast == "C" and lunch == "C" and dinner == "A":
	print("Sorry, your total calories is 2,320. You won't be able to lose 1lb.")
elif breakfast == "C" and lunch == "C" and dinner == "B":
	print("Sorry, your total calories is 1,674. You won't be able to lose 1lb.")
elif breakfast == "C" and lunch == "C" and dinner == "C":
	print("Sorry, your total calories is 1,600. You won't be able to lose 1lb.")
