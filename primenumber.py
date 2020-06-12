def prime(n):
    for i in range(2, n):
        if n % i == 0:
            print('not a prime number')
            break
    else:
        print('prime number')


prime(97)
