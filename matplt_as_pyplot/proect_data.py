import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth = 10)

plt.scatter(2.5, 4.5, s = 30, c = 10, marker = 10)

plt.xlabel("Time", fontsize = 15)
plt.ylabel("Speed", fontsize = 15)
plt.title("Differenced at time ", fontsize = 15 )
plt.tick_params(axis='both', labelsize = 15)


plt.show()

