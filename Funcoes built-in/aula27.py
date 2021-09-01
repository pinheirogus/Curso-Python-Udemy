num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

#isnumeric is digit is decimal

err1 = num1.isnumeric()
err2 = num2.isdigit()


if (err1 and err2):
    print("A soma dos números digitados é: ", int(num1)+int(num2))
else:
    print('Você digitou {0} e {1}. Um destes não é um número.'.format(num1, num2))