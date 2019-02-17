from matplotlib import pyplot as plt
from cycler import cycler
import numpy as np
path = 'dataFeb'
file = open(path, "r")
exercises = {}
numCol = 5
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
f, axarr = plt.subplots(1+int(len(exercises)/numCol), numCol, sharex=True)
f.suptitle('Exercises')
subInd = 0
def plot(name, ind,weight,reps, cind, subInd):
    col = subInd % numCol
    axarr[int(subInd/numCol), col].set_title(name)
    thicc = []
    for i in range(0,len(reps)):
        thicc.append(reps[i] ** 2.4)
    for i in range(0,len(ind)):
        axarr[int(subInd/numCol), col].scatter(ind[i], weight[i], s=thicc[i], color=colors[cind], alpha=0.7)
        axarr[int(subInd/numCol), col].text(ind[i]+0.2, weight[i], int(reps[i]), fontsize=8, alpha=0.3)
    axarr[int(subInd/numCol), col].plot(ind,weight,color=colors[cind],alpha=0.2)
colors = ['navajowhite','goldenrod','chartreuse','aquamarine','slateblue','darkviolet']
cind = 0
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
    plot(type, set_inds, weights, reps, cind, subInd)
    if cind == len(colors)-1:
        cind = 0
    cind += 1
    subInd += 1
plt.show()
