
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
  return stock_prices[x-1]

def max_price(a, b):
  values = stock_prices[a-1 : b]
  return max(values)

def min_price(a, b):
  values = stock_prices[a-1 : b]
  return min(values)


#valor no dia x
print(price_at(1))

#valor máximo da lista entre os dias a e b
print(max_price(1, 3))

#valor mínimo da lista entre os dias a e b
print(min_price(1, 3))

#valor na posição (fins de testes)
print(stock_prices[1])
