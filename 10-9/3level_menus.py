data = {
  '北京': {
    '昌平': {
      '沙河': ['oldboy', 'test'],
      '天通苑': ['链家地产', '我爱我家']
    },
    '朝阳': {
      '望京': ['oldboy', 'test'],
      '国贸': ['链家地产', '我爱我家']
    },
    '海淀': {
      '东直门': ['oldboy', 'test'],
      '天通苑': ['链家地产', '我爱我家']
    }
  },
  '广东': {
    '东莞': {},
    '常熟': {},
    '佛山': {}
  }
}
exit_flag = False
while not exit_flag:
  for i in data:
    print(i)
  choice = input('选择进入>>:')
  if choice in data:
    while not exit_flag:
      for i2 in data[choice]:
        print('\t', i2)
      choice2 = input('选择进入2>>:')
      if choice2 in data[choice]:
        while not exit_flag:
          for i3 in data[choice][choice2]:
            print('\t\t', i3)
            choice3 = input('选择进入3>>:')
            if choice3 in data[choice][choice2]:
              for i4 in data[choice][choice2][choice3]:
                print('\t\t', i4)
              choice4 = input('最后一层,按b返回>>:')
              if choice4 == 'b':
                pass  # 相当于什么也不做 占位符
              elif choice4 == 'q':
                exit_flag = True
          if choice3 == 'b':
            break
      if choice2 == 'b':
        break
