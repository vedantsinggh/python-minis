import re

def arithmetic_arranger(problems, solution = False):
	
	if (len(problems) > 5): return "Error: Too many problems."

	line1 = ""
	line2 = ""
	line3 = ""
	line4 = ""

	for problem in  problems:
		digits = re.findall("[0-9]+", problem)
		
		if len(digits) != 2: return "Error: Numbers must only contain digits."
		d1 =  int(digits[0])
		d2 =  int(digits[1])

		if 'x' in problem or '/' in problem or '%' in problem:
			return "Error: Operator must be '+' or '-'."

		del digits

		operator = '+' if ('+' in problem) else '-'
		sum = (d1 + d2) if (operator == '+') else (d1 - d2)
		numberOfSpaces = (len(str(max(d1,d2))) + 2)

		if numberOfSpaces > 6:
			return "Error: Numbers cannot be more than four digits."

		line1 = line1 + (" " * (numberOfSpaces - len(str(d1)))) + str(d1)
		line2 = line2 + operator + (" " * (numberOfSpaces - len(str(d2)) - 1)) + str(d2)
		line3 = line3 + ("-" * numberOfSpaces)
		line4 = line4 + (" " * (numberOfSpaces - len(str(sum)))) + str(sum)
		
		if problem != problems[-1]:
			line1 += " " * 4
			line2 += " " * 4
			line3 += " " * 4
			line4 += " " * 4



	arranged = line1 + "\n"  + line2 + '\n' + line3
	if solution == True:
		arranged = arranged + "\n" + line4
	return arranged

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))