def fabbicon(limits):
    a, b = 1, 1
    while a <= limits:
        print(a, end=" ")
        a, b = b, a + b


fabbicon(50)
