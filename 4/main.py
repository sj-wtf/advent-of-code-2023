power_sum = 0

with open('input_data.txt') as input_data:
  for line in input_data:
    min_colors = {"red": 0, "green": 0, "blue": 0}
    power = 0
    game_id = int(line.split(' ')[1].split(':')[0])
    game_summary_arr = line.split(':')[1].split(';')
    for pull in game_summary_arr:
      unit_counts = pull.split(',')
      for unit_count in unit_counts:
        count = unit_count.split(' ')[1].strip()
        color = unit_count.split(' ')[2].strip()
        print('color, count ' + color + ', ' + count)
        if min_colors[color] < int(count):
          min_colors[color] = int(count)

    power = min_colors['red'] * min_colors['green'] * min_colors['blue']
    power_sum += power

print('The sum of the minimum power of all game IDs is ' + str(power_sum))
