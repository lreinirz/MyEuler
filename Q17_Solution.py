ran = range(1001)
answer = 0

def letters_of_numbers(number):
	list_of_words = []
	above_thousand = number
	dummy = 0
	number = list(str(number))
	dictionary = {
		0: "",
		1: "one",
		2: "two",
		3: "three",
		4: "four",
		5: "five",
		6: "six",
		7: "seven",
		8: "eight",
		9: "nine",
		10: "ten",
		11: "eleven",
		12: "twelve",
		13: "thirteen",
		14: "fourteen",
		15: "fifteen",
		16: "sixteen",
		17: "seventeen",
		18: "eighteen",
		19: "nineteen",
		20: "twenty",
		30: "thirty",
		40: "forty",
		50: "fifty",
		60: "sixty",
		70: "seventy",
		80: "eighty",
		90: "ninety",
		100: "hundred"
	}
	for letter in number:
		while len(number) > 0:
			if len(number) == 3:
				list_of_words.extend(list(dictionary[int(number[0])]))
				if number[0] != "0":
					 list_of_words.extend(list("hundred"))				
				number.pop(0)
			elif len(number) == 2:
				if number[0] == "1":
					dummy = int(str(number[0]+str(number[1])))
					list_of_words.extend(list(dictionary[dummy]))
					number.pop(0)
					number.pop(0)					
				else:
					number[0] = number[0] + "0"
					list_of_words.extend(list(dictionary[int(number[0])]))
					number.pop(0)
			elif len(number) == 1:
				list_of_words.extend(list(dictionary[int(number[0])]))
				break
			elif int(above_thousand) >= 1000:
				list_of_words.extend(list("onethousand"))
				number.pop(0)
				break
		if above_thousand > 100 and above_thousand % 100 != 0:
			list_of_words.extend(list("and"))
	return len(list_of_words)

for values in range(1,1001):
	answer += letters_of_numbers(values)
print(f"The answer is \"{answer}\"")

#print(letters_of_numbers(121))