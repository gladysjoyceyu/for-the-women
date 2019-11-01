import csv

word_count = {}

with open('lyrics.csv') as csv_file:
	csv_reader = (csv_file)
	for line in csv_reader:
		words = line.strip("\n").split(" ")
		for word in words:
		
			# add count if word is existing
			if word in word_count:
				word_count.update({word: word_count[word] + 1})
				
			# add new word to word_count
			else:
				word_count.update({word: 1})
				
print(word_count)