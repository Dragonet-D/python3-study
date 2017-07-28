import getpass
_username = 'alex'
_password = 'abc123'
username = input("username:")
password = input("password:")
# password = getpass.getpass("password:")
if _username == username and _password == password:
  print("Welcome user {name} login...".format(name=username))
else:
  print("Invalid username or password: ")

print(username,password)