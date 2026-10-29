# NameError: name 'total' is not defined
def discount_price(initial_price, discount):
  total = initial_price - initial_price * discount
  return total

#print (total)
total_price=discount_price(100, 0.2)
print (total_price)
