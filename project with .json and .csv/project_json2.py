import json
from matplotlib import pyplot as plt

filename = 'population_data.json'

with open(filename) as file_object:
    reader = json.load(file_object)

    for read in reader:
        if read["Country Name"] == "Kazakhstan":
            years = read["Year"]
            population = int(float(read["Value"]))
            country_number = read["Country Code"]
            print(years + ":" + str(population) + " ," + country_number)


            plt.scatter(years,population,  s = 15, c = 'Blue', edgecolors= None)
            plt.xlabel("years", fontsize = 15)
            plt.ylabel("population", fontsize = 15)

plt.show()