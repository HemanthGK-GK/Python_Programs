# Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
def Harmonic(Num) :
    harmonic = 1
    # loop to apply the forumula
    for i in range(2, Num+ 1) :
        harmonic += 1 / i
 
    return harmonic
# Calling function
print(Harmonic(5))