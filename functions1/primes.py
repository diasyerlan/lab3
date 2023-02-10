def filter_prime(numbers):
    updnums = []
    for x in numbers:
        if x%2 != 0: updnums.append(x)
    for x in updnums:
        print(x)

    
    