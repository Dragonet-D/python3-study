product_list = [
  ('Iphone', 5800),
  ('Mac Pro', 9800),
  ('Bike', 800),
  ('Watch', 10600),
  ('Coffe', 31),
  ('Alex Python', 120)
]
salary = input('Input your salary:')
if salary.isdigit():
  salary = int(salary)
  while True:
    for item in product_list:
      print(item)

    break
