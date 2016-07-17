from manager import *

spread = []
filename = "weather.dat"
weather_data = read_file(filename)
del weather_data[0:2]
del weather_data[-1]

for day in weather_data:
    temperature_max = parse_data(day, 1)
    temperature_min = parse_data(day, 2)
    temperature = temperature_max - temperature_min
    spread.append(temperature)

smallest = spread.index(min(spread))

print "Day with smallest spread: ", smallest + 1
