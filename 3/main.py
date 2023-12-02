id_sum = 0

max_colors = {"red": 12, "green": 13, "blue": 14}

with open('input_data.txt') as input_data:
  for line in input_data:
    game_id = int(line.split(' ')[1].split(':')[0])
    game_summary_arr = line.split(':')[1].split(';')
    possible = True
    for pull in game_summary_arr:
      unit_counts = pull.split(',')
      for unit_count in unit_counts:
        count = unit_count.split(' ')[1].strip()
        color = unit_count.split(' ')[2].strip()
        print('color, count ' + color + ', ' + count)
        if max_colors[color] < int(count):
          possible = False
    if possible:
      print('possible game ' + str(game_id))
      id_sum += game_id

print('The sum of all possible game IDs is ' + str(id_sum))
