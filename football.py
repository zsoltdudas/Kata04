from manager import *

spread = []
filename = "football.dat"
league = read_file(filename)
del league[0]
del league[-4]

for team in league:
    goals_for = parse_data(team, 6)
    goals_against = parse_data(team, 8)
    difference = abs(goals_for - goals_against)
    spread.append(difference)

smallest = spread.index(min(spread))

print "Smallest goal difference: ", league[smallest][1]
