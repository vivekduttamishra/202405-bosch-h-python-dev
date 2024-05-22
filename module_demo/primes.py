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