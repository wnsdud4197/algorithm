# import time

# def fib(n):
#     if n<2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# t0 = time.time()
# fib(10)
# t1 = time.time()

# total = t1 - t0
# print('%.20f' % total)


sample_dit = {}

for i in enumerate(range(4)):
    sample_dit[i[0]] = i[1]

print(sum(sample_dit.values()))