nums = [11,23,43,56,78,87,66,32]

for i in nums:
    if i % 5 == 0:
        print(i)
        break

else:
    print('not found')