def uniao(arr1, arr2):
  uniao = []
  for i in arr1:
    if i not in arr2:
      uniao.append(i)
  for i in arr2:
    if i not in arr1:
      uniao.append(i)
  return uniao