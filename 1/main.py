line_digits = []

with open('input_data.txt') as input:
  for line in input:
    filterobj = filter(str.isdigit, line)
    only_digits = str("".join(filterobj))
    if (only_digits == ""):
      pass
    else:
      first_and_last = only_digits[0] + only_digits[-1]
      line_digits.append(int(first_and_last))

print("The sum of all numbers extracted from rows is " + str(sum(line_digits)))
