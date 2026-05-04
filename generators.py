num = [1,2,3,4,5,6,7,8,9]
squares=[n**2 for n in num]
evens=[n for n in num if n%2==0 ]
squares_even =[n**2 for n in num if n%2==0]
print(squares)
print(evens)
print(squares_even)
 
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b, a+b   
gen= fibonacci()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def countdown(n):
    while n > 0:
        yield n
        n -= 1

c = countdown(3)
print(next(c))  
print(next(c))  
 

    