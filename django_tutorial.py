# 제약 없이 인자를 입력하고 싶을 때

def plus(a, b, *args, **kwargs):
  print(args)
  print(kwargs)
  return a + b

plus(2,1,1,1,1,1,1,1,hello=True, df=True, fdf=True, ooo=False)



def plus(*args):
  result = 0
  for number in args:
    result += number
    
  return result

print(plus(2,4,5,6,1,23,4,5))