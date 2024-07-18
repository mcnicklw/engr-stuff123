
def hailstone(num):
    steps=0
    while num != 1:
        steps+=1
        if num % 2 == 0:
           num=num/2
        else: num = 3*num+1
    return steps
ans=hailstone(3)


