import csv
from time import strptime
import matplotlib.pyplot  as plt
from datetime import datetime

# Read Sitka weather file
# filename = './data/sitka_weather_07-2014.csv'
# filename = './data/sitka_weather_2014.csv'
filename = './data/death_valley_2014.csv'   # This file containing missing data
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get date, high, and low temperatures from file
    dates, highs, lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            low = int(row[3])
            high = int(row[1])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)       
            highs.append(high)        
            lows.append(low)

    # Plot data
    fig = plt.figure(figsize=(10,6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) 

    # Format plot
    # plt.title("Daily high and low temperatures, July 2014", fontsize=24)
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()