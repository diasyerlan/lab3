def permutations(s, l, r):
    if l == r:
        print(s)
    else :
        for i in range(l, r):
            s[l], s[i] = s[i], s[l]
            permutations(s,  l+1, r)
            s[l], s[i] = s[i], s[l]
        
x = input()
n = len(x)
a = list(x)
permutations(a, 0, n)
#abc 
