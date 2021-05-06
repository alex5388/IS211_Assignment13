def Fib(n): #fibinacci function
   if n < 0:
       print("Incorrect input")
   elif n == 0:
       return 0
   elif n == 1 or n == 2:
       return 1
   else:
       return Fib(n - 1) + Fib(n - 2) #Logic for the fibonacci series



if __name__=="__main__":
    n = int(input("Enter nth element you want to see: "))
    print(Fib(n))

def gcd(m,n):
    if m< n:
        (m,n) = (n,m)
    if(m%n) == 0:
        return n
    else:
        return (gcd(n, m % n)) # recursion taking place

if __name__=="__main__":
    m = int(input("Enter 1st number for GCD: "))
    n = int(input("Enter 2nd number for GCD: "))
    print(gcd(m,n))

def compareTO(s1, s2):
    if len(s1) < len(s2):
        return -1
    elif len(s1) == len(s2):
        return 0
    else:
        return 1

if __name__ == "__main__":
    print("""
        • -1  if s1 < s2,
        • 0 if s1 == s2
        • 1 if s1 > s2
        """)
    s1 = str(input("Enter 1st string to compare: "))
    s2 = str(input("Enter 2nd string to compare: "))
    print(compareTO(s1, s2))