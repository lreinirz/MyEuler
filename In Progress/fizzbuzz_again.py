def fizzbuzz(multi1, multi2, start = 1, end = 100, increase = 1):
    for num in range(start, end+1, increase):
        if num % multi1 == 0 and num % multi2 == 0:
            print("fizzbuzz")
        elif num % multi1 == 0:
            print("fizz")
        elif num % multi2 == 0:
            print("buzz")
        else:
            print(num)

fizzbuzz(3, 5)

'''Testing if this change sticks'''