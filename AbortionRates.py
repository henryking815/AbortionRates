import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Open CSV file containing abortion rate data
filename = 'data/as-dec-19-general-abortion-rate.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get years and rates of abortions.
    years, rates = [], []
    for row in reader:
        year = row[0]
        years.append(year)
        rate = float(row[1])
        rates.append(rate)

# Plot the abortion rates.
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(years, rates, c='red')

# Format plot.
plt.title("Abortion Rates (1980 - 2019)", fontsize=24)
plt.xlabel('Year', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("General Abortion Rates", fontsize=16)
plt.tick_params(axis='x', which='major', labelsize=8)

plt.show()

