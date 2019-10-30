#cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
# with open("cities.txt", 'w') as cityFile:
# 	for city in cities:
# 		print(city, file=cityFile)

# cities = []
#
# with open("cities.txt", 'r') as cityFile:
# 	for city in cityFile:
# 		cities.append(city.strip('\n'))
#
# print(cities)
# print(cities[0].strip('Ade'))

# imelda = "More Mayhem", "Imelda May", "2011", ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Ketnish Town Waltz"))
#
# with open("imelda.txt", 'w') as imeldaFile:
# 	print(imelda, file=imeldaFile)

with open("imelda.txt", 'r') as imeldaFile:
	contetns = imeldaFile.read()

imelda = eval(contetns)
print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(*tracks, sep='\n')