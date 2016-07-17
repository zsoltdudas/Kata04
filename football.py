from manager import *

spread = []
filename = "football.dat"
league = read_file(filename)
del league[0]
del league[-4]

for team in league:
    difference = parse_data(team, 6, 8)
    spread.append(difference)

smallest = spread.index(min(spread))

print "Smallest goal difference: ", league[smallest][1]
