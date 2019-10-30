import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beansOnToast = ["beans", "bread"]
scrambledEggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

with shelve.open("recipies") as recipies:
	# recipies["blt"] = blt
	# recipies["beans on toast"] = beansOnToast
	# recipies["scrambled eggs"] = scrambledEggs
	# recipies["pasta"] = pasta
	# recipies["soup"] = soup
 
	# recipies["blt"].append("butter")
	# recipies["pasta"].append("tomato")

	tempList = recipies["blt"]
	tempList.append("butter")
	recipies["blt"] = tempList

	for recipe in recipies:
		print(recipe, recipies[recipe])
