age_of_oldboy = 56
count = 0
while count < 3:
  guess_age = int(input("age:"))
  if guess_age == age_of_oldboy :
    print("yes,you got it")
    break
  elif guess_age > age_of_oldboy:
    print('think bigger')
  else:
    print("think smaller")
  count += 1
else:
  print("you have tried too many times . fuck off")