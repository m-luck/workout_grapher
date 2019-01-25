morning_path = "morning.txt"
afternoon_path = "afternoon.txt"
morning_file = open(morning_path, "r")
afternoon_path = open(afternoon_path, "r")
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
