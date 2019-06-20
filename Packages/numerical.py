# Functions to check if number is Prime
def is_prime(n):
    flag=1
    if n==2:
        return True
    for i in range(2,n//2+1):
        if (n%i==0):
            flag=0
            return False
        
    if flag==1:
        return True
# Functions to determine number of prime  factors     
def numberPrimeFactors(n):
    if is_prime(n):
        return 1
    count=0
    for i in range(2,n//2+1):
        if is_prime(i) and n%i==0:
            count=count+1
    return count
#isSpecialNumber(6,2)