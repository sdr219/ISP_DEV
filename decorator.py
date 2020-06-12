def div(a, b):
    print(a / b)


div(2, 4)


def smart_dev(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
            return func(a, b)

    return inner


div1 = smart_dev(div)
div1(2, 4)
