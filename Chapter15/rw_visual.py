import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Create and plot a Random Walk
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))

    # Set the size of plotting window
    plt.figure(figsize=(10,6))

    # plt.scatter(rw.x_values, rw.y_values,c=point_numbers, cmap=plt.cm.Blues,
    #     edgecolors='none' ,s=1)
    plt.plot(rw.x_values, rw.y_values, lw = 1, cmap = 0)

    # Emphasize the first and the last point
    plt.scatter(0,0, c='green', edgecolors='none', s=30)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', 
        s=30)

    # Remove the axes
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Create another Random Walk? (y/n): ")
    if keep_running == 'n':
        break