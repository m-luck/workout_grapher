filename = "line_separated_exercises.txt"
file = open(filename, "r")
exercises = {}
for line in file:
   		exercise_data = line.split(":")
   		exercise_name = exercise_data[0]
   		exercise_stats = exercise_data[1]
   		exercises[exercise_name] = exercise_stats

for name in exercises:
	stats = exercises[name]
	stat_sets = stats.split("],[")
	# print(stat_sets)
	for _set in stat_sets:
		_set.replace("75","")
		print(_set)

string = "wow"
string.replace("w","")
print(string)