import json

filename = 'population_data.json'

with open(filename) as file_object:
    reader = json.load(file_object)
    print(reader)

    for data in reader:
        if data["Year"] == "2010":
            country_name = data["Country Name"]
            population = data["Value"]
            print(country_name + ": " + population)