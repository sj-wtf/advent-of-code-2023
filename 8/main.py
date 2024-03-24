card_wins = {}

def load_data():
  with open('input_data.txt') as file:
    for line in file:
      # Splitting up each line in the file into various fields we can work with
      label, numbers = line.split(":")
      card_id = int(label.split()[1])
      winning_numbers = numbers.split('|')[0]
      number_pool = numbers.split('|')[1]
      winning_numbers = winning_numbers.split()
      number_pool = number_pool.split()
      # Type casting those fields so we can do math with them
      to_int = lambda x: int(x)
      winning_numbers = list(map(to_int, winning_numbers))
      number_pool = list(map(to_int, number_pool))
      matches = list(set(winning_numbers) & set(number_pool))
      card_wins[card_id] = list(range(card_id + 1, card_id + len(matches) + 1))

def get_won_cards_by_card_id(card_id):
  won_cards = card_wins[card_id]
  for i in won_cards:
    global total_sum 
    total_sum = total_sum + 1
    get_won_cards_by_card_id(i)


load_data()
total_sum = len(card_wins)
for card_id in card_wins:
  get_won_cards_by_card_id(card_id)

print(f'The total number of scratchoffs is {total_sum}')
