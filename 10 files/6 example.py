import shelve

books = shelve.open("book")
books["recipes"] = {"blt": ["beacon", "lettuce", "tomato", "bread"],
					"beans on toast": ["beans", "bread"],
					"scrambled eggs": ["eggs", "butter", "milk"],
					"soup": ["tin of soup"],
					"pasta": ["pasta", "cheese"]}
books["maintenance"] = {"stuck": ["oil"],
						"loose": ["gafer tape"]}

print(books["recipes"]["soup"])
print(books["recipes"]["scrambled eggs"])

print(books["maintenance"]["loose"])
books.close()