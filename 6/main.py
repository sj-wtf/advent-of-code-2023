filechars = []
gear_factors = []

with open('input_data.txt') as input:
  for line in input:
    filechars.append(list(line))

# This is a bit dense

for x, line in enumerate(filechars):
  for y, character in enumerate(line):
    if character == '*':
      # print(f'Identified * character at {x} {y}')
      x_search_indexes = [idx for idx in range(x - 1, x + 2) if idx >= 0 and idx <= len(filechars) - 1]
      y_search_indexes = [idx for idx in range(y - 1, y + 2) if idx >= 0 and idx <= len(line) - 1]
      factors = []
      print(f'Searching for adjacent numbers at x = {x_search_indexes}, and y = {y_search_indexes}')
      for x_idx in x_search_indexes:
        for y_idx in y_search_indexes:
          if filechars[x_idx][y_idx].isdigit():
            # print(f'Found number {filechars[x_idx][y_idx]}, seeking towards beginning')
            # Seek to beginning of number
            while filechars[x_idx][y_idx].isdigit():
              y_idx -= 1
            else:
              # Go back to the beginning of the number and start accumulating digits
              y_idx += 1
              accumulated_number = []
              # print(f'Beginning of number identified at {x_idx}, {y_idx}')
              while filechars[x_idx][y_idx].isdigit():
                accumulated_number.append(filechars[x_idx][y_idx])
                y_idx += 1
              else:
                # Once finished accumulating the number, append it to a list of factors
                factors.append(int(''.join(accumulated_number)))

      factors = list(dict.fromkeys(factors))
      print(f'Deduplicated factors {factors}')
      # it's only a gear ratio if there are exactly 2
      if len(factors) == 2:
        gear_factors.append(factors[0] * factors[1])

print(sum(gear_factors))
