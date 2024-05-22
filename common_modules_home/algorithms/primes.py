def is_prime(number):
    if number<2:
        return False
    
    for x in range(2,number):
        if number % x == 0:
            return False
    
    return True


def prime_range_list(min,max):
    result = []
    for number in range(min,max+1):
        if is_prime(number):
            result.append(number)
    return result


def test_is_prime():
    test_data={ 2:True, 3: True, 4: False, -2:False, 11:True, 14:False}
    for number,expected in test_data.items():
        actual = is_prime(number)
        if actual != expected:
            print(f'FAILED for is_prime({number}): exepected={expected} got {actual}')
        else:
            print(f'PASSED for is_prime({number}):')


if __name__ == '__main__':
    #run the test only when loaded directly.
    print('running primes app')
    test_is_prime()
else:
    print('loading primes module...')