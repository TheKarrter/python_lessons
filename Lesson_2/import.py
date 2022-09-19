import functions as func

print(func.f(1))

print(func.new_string('A'))
print(func.new_string('A',6))
print(func.new_string(5))

print(func.concatenation('a','b','c','d','e'))
print(func.concatenation('a', '1'))

list = []
for e in range(1,10):
    list.append(func.fib(e))
print(list)