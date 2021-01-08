def fizzbuzz():
    n = int(input('enter a number'))
    print(n)
    new_set = list(range(n + 1))
    for i in new_set:
        new_num = new_set[i]
        if new_num % 3 == 0:
            print('fizz')
        elif new_num  % 5 == 0:
            print('buzz')
        elif new_num % 3 == 0 and new_num % 5 == 0:
            print('fizzbuzz')
        else:
            print(new_num)

fizzbuzz()