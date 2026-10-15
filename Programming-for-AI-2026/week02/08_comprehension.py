squares=[]
for i in range(1,20):
  squares.append(i*i)
print(squares)
print()

Squares=[i*i for i in range(1,20)]
print(Squares)
print()

even=[]
odd=[]
for i in range(1,50):
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)
print(odd)
print(even)
print()

Even=[i for i in range(1,50) if i%2==0]
Odd=[x for x in range(1,50) if x%2!=0]
print(Odd)
print(Even)