import random
import numpy as np
import csv
import matplotlib.pyplot as plt


def cal_pi():
    # read user's input
    num_of_points = [20, 50, 100, 200, 300, 500, 1000, 5000]
    # csv version
    csv_file = open("Question1.csv", "w")
    writer = csv.writer(csv_file)
    writer.writerow(['number of points', 'mean', 'variance'])
    # arrays
    mean_array = []
    var_array = []
    # 8 n
    for i in range(8):
        # plt.figure(i, figsize=(4, 4))
        temp = []
        # 20 times
        for t in range(100):
            inside = 0
            for j in range(num_of_points[i]):
                x = random.random()
                y = random.random()
                # inside the quarter of circle
                if x*x+y*y <= 1:
                    inside = inside + 1
                    # plot the discrete random points in the circle
                    # plt.plot(x, y, 'ro', color="red")
                # else:
                    # plt.plot(x, y, 'ro', color="blue")
            pi = inside * 4 / num_of_points[i]
            temp.append(pi)
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
    plt.xlabel("N")  # X轴标签
    plt.ylabel("Mean")  # Y轴标签
    plt.savefig('Q1_Mean.png')
    plt.figure(2)
    plt.title("The Trend of the Variances as N changes")
    plt.plot(num_of_points, var_array, "g--", linewidth = 1)
    plt.xlabel("N")  # X轴标签
    plt.ylabel("Variance")  # Y轴标签
    plt.savefig('Q1_Variance.png')


cal_pi()
