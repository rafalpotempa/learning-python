import shelve

with shelve.open("bike") as bike:
	bike["make"] = "Honda"
	bike["model"] = "250 dream"
	bike["color"] = "red"
	bike["engineSize"] = 250
	bike["enginSize"] = 250

	del bike["enginSize"]

	for key in bike:
		print(f"{key:12}: {bike[key]}")
