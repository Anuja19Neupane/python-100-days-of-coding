import sys

def is_prime(number:int):
    for num in range(2,int(number/2)+1):
        if number%num==0:
            return False
    
    return True


print("hello anuja")
print(__name__)
if __name__=="__main__":
    print("hello")
    prime=is_prime(int(sys.argv[1]))
    print(prime)

        