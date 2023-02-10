def hist(list):
    for item in list:
        for i in range(item):
            print('*', end='')
        print('\n')
list = [4, 9, 7]
hist(list)