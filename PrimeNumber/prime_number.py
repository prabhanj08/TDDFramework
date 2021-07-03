
def prime_number(num):
    if num == 1 :
        return "Not Prime"
    elif num < 0 or num == -0:
        return "negative input"
    elif num is None:
        return "Empty input"

    for i in range (2,num):
        if num%i == 0:
            return "Not Prime"
    return "Prime Number"
