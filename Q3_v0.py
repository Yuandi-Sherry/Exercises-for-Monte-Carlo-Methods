import random
import numpy as np
import csv
import math


def cal_int():
    num_of_points = [5, 10, 20, 30, 40, 50, 60, 70, 80, 100, 200000]
    # ---------array version---------
    # results = []
    # ---------array version---------
    # csv version
    csv_file = open("test3.csv", "w")
    writer = csv.writer(csv_file)
    writer.writerow(['number of points', 'mean', 'variance'])
    # 8 n
    for i in range(len(num_of_points)):
        temp = []
        # 20 times
        for t in range(100):
            vol = 0
            for j in range(num_of_points[i]):
                x = random.random() * 2 + 2
                y = random.random() * 2 - 1
                z = (pow(y, 2) * math.exp(-pow(y, 2)) + pow(x, 4) * math.exp(-pow(x, 2))) / (x * math.exp(-pow(x, 2)))
                vol = vol + (4 - 2) * (1 - (-1)) * z
            vol = vol/num_of_points[i]
            temp.append(vol)
        mean = np.mean(temp)
        var = np.var(temp)
        row = [num_of_points[i], mean, var]
        writer.writerow(row)
        # results.append(temp)

    # calculate mean and variance
    csv_file.close()
    print('Calculation is finished. Please check out test.csv for the results')


cal_int()
