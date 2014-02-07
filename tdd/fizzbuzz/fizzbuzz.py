def fizzbuzz(num):
    if not(num % 5) and not(num % 3):
        return "fizzbuzz"
    elif not(num % 3):
        return "fizz"
    elif not(num % 5):
        return "buzz"
    else:
        return num
