def primeX(x):
    count = 0
    num = 1
    while True:
        num += 1
        if prime_number(num):
            count += 1
            if count == x:
                return num

def prime_number(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29