import re

summation = 0

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

filter = "(?=(" + "|".join(numbers) + "|\\d))"

def locate(x):
  if x in numbers:
    return str(numbers.index(x) +1)
  return x

with open('input_data.txt') as textfile:
  for line in textfile:
    digits = [*map(locate, re.findall(filter, line))]
    summation += int(digits[0] + digits[-1])

print("the sum total is " + str(summation))
