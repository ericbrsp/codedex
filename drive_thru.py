menu_list = ['Cheeseburger', 'Fries', 'Soda', 'Ice Cream', 'Cookie']

def welcome():
  print ('Escolha um dos itens: 1) Cheeseburger | 2) Fries | 3) Soda | 4 Ice Cream | 5) Cookie ')


def get_item(a):
  item = int(input(a))
  if item == 1:
    print(menu_list[0])
  elif item == 2:
    print(menu_list[1])
  elif item == 3:
    print(menu_list[2])
  elif item == 4:
    print(menu_list[4])
  elif item == 5:
    print(menu_list[4])
  else:
    print('Este item não existe')

welcome()

get_item('Escolha pelo número: ')
