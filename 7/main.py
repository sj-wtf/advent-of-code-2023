scores = []

with open('input_data.txt') as file:
  for line in file:
    card_score = 0
    winning_numbers, available_numbers = line.split(':')[1].split('|')
    winning_numbers = winning_numbers.strip().split(' ')
    winning_numbers = set([i for i in winning_numbers if i])
    available_numbers = available_numbers.strip().split(' ')
    available_numbers = set([i for i in available_numbers if i])
    # print(f'Winning numbers found in available numbers: {winning_numbers.intersection(available_numbers)}')
    win_count = len(winning_numbers.intersection(available_numbers))
    # print(f'There are {win_count} matching winning numbers in the available pool')
    if win_count == 1:
      card_score = 1
    if win_count > 1:
      card_score = 1
      for i in range(win_count - 1):
        card_score = card_score * 2
    print(f'This card is worth {card_score} points')
    scores.append(card_score)

print(f'The total points in the stack of scratchoffs is {sum(scores)}')
