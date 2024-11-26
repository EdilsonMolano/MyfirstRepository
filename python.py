n = float(input())
pi = 1
iteracion = 1
for denominador in range(3, n, 2):
  if iteracion % 2 != 0:
    pi -= 1/denominador
  else:
    pi += 1/denominador
pi = pi*4

print(f"the result is {pi:.10f}")
