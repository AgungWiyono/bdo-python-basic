import matplotlib.pyplot as plt

import json
import csv

from config import SAVEFILE


plot_data = {}
key_names = []

with open(SAVEFILE) as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count==0:
            for key in row:
                plot_data[key] = []
            key_names = list(plot_data.keys())
            line_count += 1
        else:
            for number, value in enumerate(row):
                if number!=0:
                    value = float(value)
                plot_data[key_names[number]].append(value)


def normalize_column(data):
    min_n = min(data)
    max_n = max(data)

    standardized_data = [(n - min_n) / (max_n - min_n) for n in data]
    return standardized_data


# Standardized data from file
for key in key_names[1:]:
    plot_data[key] = normalize_column(plot_data[key])


for number in range(1, len(key_names)):
    plt.plot(plot_data[key_names[0]],
             plot_data[key_names[number]],
             label=key_names[number])

plt.legend(title="Pergerakan mata uang")
plt.xticks(rotation=40)
plt.show()
