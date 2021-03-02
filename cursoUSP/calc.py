




def num_fat(i):
    result = 1
    while i >= 1:
        result = result * i
        i = i - 1
    return result

def numerobinomial(num1,num2):
    return num_fat(num1) // num_fat(num2) * (num_fat(num1-num2))

num1 = int(input("Digite o valor do primeiro número binomial: "))
num2 = int(input("Digite o valor do segundo número binomial: "))

print ("O número binomial é: ", numerobinomial(num1,num2))
