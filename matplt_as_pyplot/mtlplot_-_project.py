import matplotlib.pyplot as plt
from data_random_project import RandomWalk

while True:
    rw = RandomWalk(500)

    rw.fill_walk()
    points = list(range(rw.num_points))

    #plt.plot(rw.x_values, rw.y_values, linewidth = 10)
    plt.scatter(rw.x_values, rw.y_values, s=10, c=points, edgecolors=None, cmap=plt.cm.Blues)
    plt.scatter(0, 0, s=100, c='Red', edgecolors=None)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], s=100, c='Green', edgecolors=None)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.axis([0, 600, 0, 600])
    plt.xlabel("x values", fontsize=15)
    plt.ylabel("y label", fontsize=15)
    plt.title("LIST")
    plt.tick_params(axis='both', labelsize=15)
    #plt.figure(dpi=128, figsize=(10, 6))
    plt.show()

    keep_running = input("Continue cycle while y/n :")
    if keep_running == 'n':
        break
    else:
        continue
