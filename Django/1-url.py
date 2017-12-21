from wsgiref.simple_server import make_server


def handle_index():
  return ['<h1>Hello, Index !</h1>'.encode('utf-8'), ]


def handle_date():
  return ['<h1>Hello, Date !</h1>'.encode('utf-8'), ]


ULR_DICT = {
  '/index': handle_index,
  '/date': handle_date
}


def RunServer(environ, start_response):
  # environ 客户端发来的所有数据
  # start_response 封装要返回给用户的数据,响应头状态
  start_response('200 OK', [('Content-Type', 'text/html')])
  current_url = environ['PATH_INFO']
  if current_url == '/index':
    return handle_index()
  elif current_url == '/date':
    return handle_date()
  else:
    # 返回内容
    return ['<h1>404 !</h1>'.encode('utf-8'), ]


'''
import hashlib
m = hashlib.md5()
# 变字节
# b'ffff'
#bytes('ffff',encoding = 'utf-8')
m.update(b'fffff')
ret = m.hexdigest()
print(ret)
'''

if __name__ == '__main__':
  httpd = make_server('', 8000, RunServer)
  print('Server HTTP on port 8000...')
  httpd.serve_forever()
