import shelve

with shelve.open("shelftest") as fruits:
	fruits["orange"] = "a sweet, orange, citrus fruit"
	fruits["apple"] = "good for making cider"
	fruits["lemon"] = "a sour, yellow citrus fruit"
	fruits["lime"] = "a sour, green citrus fruit"

	##

	fruits["lime"] = "great with tequila"
	
	for fruit in fruits:
		print(f"{fruit:10}: {fruits[fruit]}")

	while True:
		shelfKey = input("Please enter a fruit: ")
		if shelfKey == "quit":
			break
		elif shelfKey == "":
			continue
		print(fruits.get(shelfKey, f"{shelfKey} not specified"))
