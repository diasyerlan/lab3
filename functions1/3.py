def solve(numheads, numlegs):
    numchicken = int((numlegs - 4*numheads)/(-2))
    numrabbit = int(numheads - numchicken)
    print('rabbits: ' + str(numrabbit))
    print('chickens: ' + str(numchicken))
    
solve(35, 94)
