n = int(input("Enter the terms you want to be printed "))

def fibo(n):                          #without recursion
    if n<=0:
        print("cannot be printed")
    elif n==1:
        print(0)
    else:
        l = [0,1]
        for i in range(0,n):
            print(l[i])
            if i>0:
                l.append(l[i]+l[i-1])

fibo(n)
            
def recur_fibo(n):           #with recursion
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return recur_fibo(n-1)+recur_fibo(n-2)
    
for i in range(0,n):
    print(recur_fibo(i))

