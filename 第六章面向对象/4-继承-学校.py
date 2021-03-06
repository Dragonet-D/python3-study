class School(object):
  '''object 是基类'''

  def __init__(self, name, addr):
    self.name = name
    self.addr = addr
    self.students = []
    self.teachers = []
    self.staffs = []

  def enroll(self, stu_obj):
    print('为学员 %s 办理注册手续' % stu_obj.name)
    self.students.append(stu_obj)

  def hire(self, staff_obj):
    self.staffs.append(staff_obj)
    print('雇佣新员工 %s' % staff_obj.name)


class SchoolMember(object):
  def __init__(self, name, age, sex):
    self.name = name
    self.age = age
    self.sex = sex

  def tell(self):
    pass


class Teacher(SchoolMember):
  def __init__(self, name, age, sex, salary, course):
    super(Teacher, self).__init__(name, age, sex)
    self.salary = salary
    self.course = course

  def tell(self):
    print('''
    ----- info of Rracher: %s-----
          Name: %s
          Age: %s
          Sex: %s
          Salary: %s
          Course: %s
    ''' % (self.name, self.name, self.age, self.sex, self.salary, self.course))

  def teach(self):
    print('%s is teaching course[%s]' % (self.name, self.course))


class Student(SchoolMember):
  def __init__(self, name, age, sex, stu_id, grade):
    super(Student, self).__init__(name, age, sex)
    self.stu_id = stu_id
    self.grade = grade

  def tell(self):
    print('''
    ----- info of Rracher: %s-----
          Name: %s
          Age: %s
          Sex: %s
          stu_id: %s
          grade: %s
    ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

  def pay_tuition(self, amount):
    print('%s has paid tution for %s' % (self.name, amount))


school = School('老男孩IT', '沙河')
t1 = Teacher('Oldboy', 56, 'MF', 2000, 'Linux')
t2 = Teacher('Alex', 22, 'M', 3000, 'PythonDevOps')
s1 = Student('陈荣华', 36, 'MF', 1001, 'PythonDevOps')
s2 = Student('徐良伟', 19, 'M', 1002, 'PythonDevOps')
t1.tell()
s1.tell()
school.hire(t1)
school.enroll(s1)
print(school.students)
print(school.staffs)
school.staffs[0].teach()

for stu in school.students:
  stu.pay_tuition(5000)
