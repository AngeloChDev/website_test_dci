
def doit(email):
      c={'email':email}
      print(c, type(c))
      with open('./new.txt', 'w') as f:
            f.write(email)
      