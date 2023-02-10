def rev(s):
    b = s.split(" ")
    b.reverse()
    for x in b:
        print(x, end = " ")
s = input()
rev(s)
    