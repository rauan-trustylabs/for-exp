import csv
from matplotlib import pyplot as plt
from datetime import datetime
#часть кода с csv, я изменил пример, и добавил в него класс
class Weather():
    def __init__(self, filename = 'weather.csv'):
        self.filename = filename

    def reader_csv(self):
        with open(self.filename) as file_object:
            reader = csv.reader(file_object)
            read = next(reader)
            dates, highs = [], []
            for row in reader:
                date = datetime.strptime(row[0], "%Y-%m-%d")
                dates.append(date)
                print(dates)
                high = int(row[1])
                highs.append(high)
                print(highs)


#часть кода с matplotlib
        fig = plt.figure(dpi=128, figsize= (10, 6))
        plt.plot(dates, highs,  c = 'red')
        fig.autofmt_xdate()
        plt.title("Analyze ", fontsize = 15)
        plt.xlabel(" DATES", fontsize=15)
        plt.ylabel("Temperature", fontsize=15)
        plt.tick_params(axis='both')

        plt.show()


my_weather = Weather()
my_weather.reader_csv()








