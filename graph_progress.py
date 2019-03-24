from matplotlib import pyplot as plt
from cycler import cycler
import numpy as np
path = 'data'
file = open(path, "r")
exercises = {}
graph = True
numCol = 5
all_names = []
def parse_line(line):
    '''
    line:a string from the data file
    returns a tuple of str:exercise_name and str:exercises_stats
    '''
    exercise_data = line.split(":")
    exercise_name = exercise_data[0]
    exercise_stats = exercise_data[1].split(",")
    return exercise_name, exercise_stats
for line in file:
    exercise_name, exercise_stats = parse_line(line)
    exercises[exercise_name] = exercise_stats
    all_names.append(exercise_name)
f, axarr = plt.subplots(1+int(len(exercises)/numCol), numCol, sharex=True)
f.suptitle('Exercises')
subInd = 0
def plot(name, ind,weight,reps, cind, subInd):
    col = subInd % numCol
    axarr[int(subInd/numCol), col].set_title(name)
    thicc = []
    for i in range(0,len(reps)):
        thicc.append(reps[i] ** 1.8)
    for i in range(0,len(ind)):
        axarr[int(subInd/numCol), col].scatter(ind[i], weight[i], s=thicc[i], color=colors[cind], alpha=0.7)
        axarr[int(subInd/numCol), col].text(ind[i]+0.2, weight[i], int(reps[i]), fontsize=8, alpha=0.3)
    axarr[int(subInd/numCol), col].plot(ind,weight,color=colors[cind],alpha=0.2)
colors = ['navajowhite','goldenrod','chartreuse','aquamarine','slateblue','darkviolet']
cind = 0
all_weights = []
all_reps = []
single_names = []
single_weights = []
single_reps = []
for type in exercises: # Iterate through exercises
    weights = []
    reps = []
    set_ind = 0
    set_inds = []
    for stat in exercises[type]: # Iterate through exercises' weightsXreps
        exer_data = stat.split("x")
        print("{name} {0}x{1}".format(exer_data[0],exer_data[1],name=type))
        if len(exer_data)>1:
            weight = float(exer_data[0])
            rep = float(exer_data[1])
            weights.append(weight)
            reps.append(rep)
            set_inds.append(set_ind)
            set_ind += 1
            single_names.append(type)
            single_weights.append(weight)
            single_reps.append(rep)
    all_weights.append([*weights])
    all_reps.append([*reps])
    plot(type, set_inds, weights, reps, cind, subInd)
    if cind == len(colors)-1:
        cind = 0
    cind += 1
    subInd += 1
if graph==True: plt.show()

import numpy
import pandas as pd
# Uncomment here to output a csv for data processing
print("W")
print(*all_weights, sep="\n")
print("R")
print(*all_reps, sep="\n")
print("N")
print(*all_names, sep="\n")
df = pd.DataFrame({"n" : single_names, "w" : single_weights, "r" : single_reps})
df.to_csv("out.csv", index=False)
