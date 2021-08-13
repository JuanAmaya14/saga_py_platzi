def is_prime(number: int) -> bool:
    result: bool = True
    for x in range(2,number):
        if number % x == 0:
            result = False
            break
    return result

def run():
    print(is_prime(4))

if __name__ == '__main__':
    run()