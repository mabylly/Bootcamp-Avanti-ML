def primos(arr):
  primos = []
  for i in arr:
    if i > 1:
      for j in range(2, i):
        if (i % j) == 0:
          break
      else:
        primos.append(i)
  return primos