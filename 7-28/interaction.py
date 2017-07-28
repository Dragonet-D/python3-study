username = input("suername:")
#raw_input  input
passworld = input("passworld:")
age = int(input("Age:"))
#print(type(age),type(str(age)))
job = input("Job:")
salary = int(input("salary:"))
#print(username,passworld)
info = '''
-------------info of %s----------
username: %s
age:%d
job:%s
salary:%s
'''% (username,username,age,job,salary)
#print(info)
info2 = '''
----------info of {_username}----------
  name:{_username}
  age:{_age}
  job:{_job}
  salary:{_salary}
'''.format(_username=username,
            _age=age,
            _job=job,
           __salary=salary )
print(info2)
info3 = '''
----------info of {0}----------
  name:{0}
  age:{1}
  job:{2}
  salary:{3}
'''.format(username,age,job,salary)

