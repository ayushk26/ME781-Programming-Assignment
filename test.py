def get_primenumbers(n):
  result = []
  try:
    n = int(float(n))
    if n > 2:
      result.append(2)
    for i in range(3,n):
        for p in result:
            if i%p == 0:
                break
            elif p == result[-1]:
                result.append(i)
    print(result)
  except ValueError:
    print("Wrong input")

get_primenumbers('1')