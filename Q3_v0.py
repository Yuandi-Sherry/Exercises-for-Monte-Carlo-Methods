import random
import numpy as np
import csv
import math
import matplotlib.pyplot as plt


def cal_int():
    mean_array = []
    var_array = []
    num_of_points = [10, 20, 30, 40, 50, 60, 70, 80, 100, 200, 500]
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
        # calculate mean and variance
        mean_array.append(np.mean(temp))
        var_array.append(np.var(temp))
        row = [num_of_points[i], mean_array[len(mean_array) - 1], var_array[len(var_array) - 1]]
        writer.writerow(row)
    csv_file.close()
    # calculation finished
    # the following is plotting the figure
    plt.figure(1)
    plt.title("The Trend of the Results as N changes")
    plt.plot(num_of_points, mean_array, "b--", linewidth = 1)
    # plt.plot(num_of_points, var_array, "r--", linewidth = 1)
    plt.xlabel("N")  # X轴标签
    plt.ylabel("Mean")  # Y轴标签
    plt.show()
    plt.figure(2)
    plt.title("The Trend of the Variances as N changes")
    plt.plot(num_of_points, var_array, "g--", linewidth = 1)
    plt.xlabel("N")  # X轴标签
    plt.ylabel("Variance")  # Y轴标签
    plt.show()


cal_int()
