age_of_oldboy = 56
count = 0
while count < 3:
  guess_age = int(input("guess age:"))
  if guess_age > age_of_oldboy:
    print("older")
  elif guess_age < age_of_oldboy:
    print("smaller")
  else:
    print("you got it")
    break
  count += 1
  if count == 3:
    continue_confirm = str(input("do you want to keep guess..?"))
    if continue_confirm == 'n':
      count = 0
