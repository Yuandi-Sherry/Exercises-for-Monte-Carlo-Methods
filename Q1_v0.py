import random
import numpy as np
import csv


def cal_pi():
    # read user's input
    num_of_points = [20, 50, 100, 200, 300, 500, 1000, 5000]
    # ---------array version---------
    # results = []
    # ---------array version---------
    # csv version
    csv_file = open("test.csv", "w")
    writer = csv.writer(csv_file)
    writer.writerow(['number of points', 'mean', 'variance'])
    # 8 n
    for i in range(8):
        temp = []
        # 20 times
        for t in range(20):
            inside = 0
            for j in range(num_of_points[i]):
                x = random.random()
                y = random.random()
                # inside the quarter of circle
                if x*x+y*y <= 1:
                    inside = inside + 1
            pi = inside * 4 / num_of_points[i]
            temp.append(pi)
        mean = np.mean(temp)
        var = np.var(temp)
        row = [num_of_points[i], mean, var]
        writer.writerow(row)
        # results.append(temp)

    # calculate mean and variance
    csv_file.close()
    print('Calculation is finished. Please check out test.csv for the results')


cal_pi()
