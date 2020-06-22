def gcd(a, b):
    while True:
        if a > b:
            a = a%b
        elif b >a:
            b = b%a
        if a == 0:
            return b
        if b==0:
            return a
    
    
   
        
def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
