filechars = []
part_numbers = []

with open('input_data.txt') as input:
  for line in input:
    filechars.append(list(line))

# This is a bit dense

for x, line in enumerate(filechars):
  accumulated_number = []
  for y, character in enumerate(line):
    if not character.isdigit():
      if accumulated_number:
        candidate_part_number = ''.join(accumulated_number)
        candidate_pass = False
        accumulated_number = []
        # Create a range that has an extra index on both sides to account for diagonal
        # characters, then get to searching for non-'.' characters in the rows around
        y_indexes = [idx for idx in range(y - len(candidate_part_number) - 1, y + 1) if idx >= 0 and idx <= len(line) - 1]
        x_indexes = [idx for idx in range(x - 1, x + 2) if idx >= 0 and idx <= len(filechars) - 1]
        print(f'Y indexes: {y_indexes}, X indexes: {x_indexes}')
        for y_idx in y_indexes:
          for x_idx in x_indexes:
            if not filechars[x_idx][y_idx].isdigit() and filechars[x_idx][y_idx] != '.' and filechars[x_idx][y_idx] != '\n':
              candidate_pass = True

        if candidate_pass:
          print(f'Candidate {candidate_part_number} passed!')
          part_numbers.append(int(candidate_part_number))
        else:
          print(f'Candidate {candidate_part_number} failed.')

    else:
      accumulated_number.append(character)

print(sum(part_numbers))
