#Test technique Fruition Sciences

#Setting up all variables and checking sent file. 
def setup():
  with open("instructions.txt") as file:
    lines =[line.split() for line in file]

  try:
    #creating a dictionnary translating values and keys from alpha to logical number.
    cardinals = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3}

    floor_x = int(lines[0][0])
    floor_y = int(lines[0][1])

    pos_x = int(lines[1][0])
    pos_y = int(lines[1][1])
    start_dir = lines[1][2]
    directions_list = lines[2][0]

  #give current_dir the value it has in dictionnary for an easier use. 
    current_dir = cardinals[start_dir]
  except:
    print("Not a valid file. Try again.")
    exit()
  
  return cardinals, floor_x, floor_y, pos_x, pos_y, start_dir, directions_list, current_dir

#Program main loop analyzing inputs and moving vacuum
def loop(cardinals, floor_x, floor_y, pos_x, pos_y, start_dir, directions_list, current_dir):

  for instruction in directions_list:
    if instruction == 'D':
      current_dir += 1
      if current_dir == 4:
        current_dir = 0
    elif instruction == 'G':
      current_dir -= 1
      if current_dir == -1:
        current_dir = 0
    elif instruction == 'A':
      if current_dir == 0 and pos_y < floor_y:
        pos_y += 1
      if current_dir == 1 and pos_x < floor_x:
        pos_x += 1
      if current_dir == 2 and pos_y > 0:
        pos_y -= 1
      if current_dir == 3 and pos_x > 0:
        pos_x -= 1

#Translating back numbers in alphabetical values by reversing the dictionnary results
  for key, value in cardinals.items():
    if value == current_dir:
      final_dir = key
  print(pos_x, pos_y, final_dir)

#Main that get the setup function and start the loop. 
if __name__ == "__main__":
  cardinals, floor_x, floor_y, pos_x, pos_y, start_dir, directions_list, current_dir = setup()
  loop(cardinals, floor_x, floor_y, pos_x, pos_y, start_dir, directions_list, current_dir)
