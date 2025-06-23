class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = True



bobs_burgers = Restaurant()

bobs_burgers.name = 'Bobs Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False


joaquins_burgers = Restaurant()

joaquins_burgers.name = 'Joaquins Burgers'
joaquins_burgers.category = 'American Diner'
joaquins_burgers.rating = 4.9
joaquins_burgers.delivery = True


bk_burgers = Restaurant()

bk_burgers.name = 'Burger King'
bk_burgers.category = 'American Diner'
bk_burgers.rating = 4.9
bk_burgers.delivery = True


print(vars(bobs_burgers))



