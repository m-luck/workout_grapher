filename = "logs.txt"
file = open(filename, "r")
for line in file:
   meals = line.split("],[")
   for meal in meals:
   		ingredients = meal.split(",")
   		for food in ingredients:
   			