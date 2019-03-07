import random
import numpy as np
import csv
import matplotlib.pyplot as plt


def cal_int():
    mean_array = []
    var_array = []
    num_of_points = [5, 10, 20, 30, 40, 50, 60, 70, 80, 100]
    # csv version
    csv_file = open("test2.csv", "w")
    writer = csv.writer(csv_file)
    writer.writerow(['number of points', 'mean', 'variance'])
    # 8 n
    for i in range(len(num_of_points)):
        temp = []
        # 100 times
        for t in range(100):
            area = 0
            for j in range(num_of_points[i]):
                x = random.random()
                y = pow(x, 3)
                area = area + y
            area = area/num_of_points[i]
            temp.append(area)
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
    plt.plot(num_of_points, mean_array, "b--", linewidth=1)
    # plt.plot(num_of_points, var_array, "r--", linewidth = 1)
    plt.xlabel("N")  # X轴标签
    plt.ylabel("Mean")  # Y轴标签
    plt.show()
    plt.figure(2)
    plt.title("The Trend of the Variances as N changes")
    plt.plot(num_of_points, var_array, "g--", linewidth=1)
    plt.xlabel("N")  # X轴标签
    plt.ylabel("Variance")  # Y轴标签
    plt.show()


cal_int()
