

def saudacao(msg, nome):
    print("{0}, {1}!".format(msg, nome))

def soma(num1, num2, num3):
    result = num1 + num2 + num3
    print(result)
    return result

def aumento_percentual(num1, perc):
    result = num1 + (num1 * perc)
    return result

def fizzBuzz(num1):
    if num1 % 3 == 0 and num1 % 5 ==0:
        return "fizzBuzz"
    elif num1 % 3 == 0:
        return "fizz"
    elif num1 % 5 == 0:
        return "Buzz"
    else:
        return num1

saudacao("Olá", "Gustavo")
soma(1, 2, 3)
print(aumento_percentual(100, 0.1))
print(fizzBuzz(4))