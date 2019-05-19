file = open('expenses.txt', 'r')

expense_strings = [line.strip() for line in file if line.strip() != '']

categories = {}

for line_item in expense_strings:
	line_item = [item.strip() for item in line_item.split(',')]

	date = line_item[0]
	price = float(line_item[1].strip('$'))
	name = line_item[2]
	category = line_item[3]

	if category in categories:
		categories[category].append((name, price))
	else:
		categories[category] = [(name, price)]

for category in categories:
	items = categories[category]
	total = sum([item[1] for item in items])

	items = sorted(items, key=lambda item: item[0])
	print(category)

	for item in items:
		print('\t', item[0], f'${item[1]}')
	print(f'${total}\n')
