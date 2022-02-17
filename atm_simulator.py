#ATM simulator
#n = paper notes
value = int(input("How much?: "))
current_total = value
n_value = 50
n_total = 0
while True:
  if(current_total >= n_value):
    current_total -= n_value
    n_total += 1
  else:
    if(n_total > 0):
      print(f"Total of {n_total} notes of ${n_value}")
    if(n_value == 50):
      n_value = 20
    elif(n_value == 20):
      n_value = 10
    elif(n_value == 10):
      n_value = 1
    n_total = 0
    if(current_total == 0):
      break
