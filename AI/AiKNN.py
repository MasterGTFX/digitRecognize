import csv
import math
import operator
import time

with open('data/train_data.csv', 'r') as csv_data:
    print("Loading train data...")
    csv_data_reader = csv.reader(csv_data)
    learn_data = []
    for row in csv_data_reader:
        learn_data.append([int(x) for x in row])
    print("Train data loaded")

with open('data/test_data.csv', 'r') as csv_data:
    print("Loading test data...")
    csv_data_reader = csv.reader(csv_data)
    test_data = []
    for row in csv_data_reader:
        test_data.append([int(x) for x in row])
    print("Test data loaded\n")


def euclideanDistance(instance1, instance2):
    distance = 0
    for x in range(len(instance1)):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


def getResponse(neighbors):
    numberVotes = {}
    for index in range(len(neighbors)):
        response = neighbors[index]
        if response in numberVotes:
            numberVotes[response] += 1
        else:
            numberVotes[response] = 1
    sortedNumberVotes = sorted(numberVotes.items(), key=operator.itemgetter(1))
    print(sortedNumberVotes)
    return sortedNumberVotes[-1][0]


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance[1:], trainingSet[x][1:])
        distances.append((trainingSet[x][0], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


trainSet = learn_data
k = 3


def testAI(trainSet, testInstance, k):
    time_start = time.time()
    neighbors = getNeighbors(trainSet, testInstance, k)
    response = getResponse(neighbors)
    print("Got:", response, "Correct:", testInstance[0], "Time:", time.time() - time_start)


def useAI(testInstance):
    time_start = time.time()
    neighbors = getNeighbors(trainSet, testInstance, k)
    response = getResponse(neighbors)
    print("Got:", response, "Time:", time.time() - time_start)
