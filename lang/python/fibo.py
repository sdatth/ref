#using recurison
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibo(i))


# using normal method

n1 = 0
n2 = 1
nterms = 10

if nterms <= 0:
    print("please enter positive integer")

else:
    while nterms > 0:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        nterms -= 1
