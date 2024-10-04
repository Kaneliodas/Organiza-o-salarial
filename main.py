#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input("Qual o seu salário atual para que possamos fazer o seu reajuste: "))
if (salario < 280):
    percentual = 0.20*salario
    salario2 = salario + 0.20*salario
    print("Seu antigo salário  é: " ,salario)
    print("O percentual adicionado ao seu salário é: " ,percentual)
    print("Seu novo salário agora é: " ,salario2)
    
elif (salario >= 280 and salario < 700):
    percentual = 0.15*salario
    salario2 = salario + 0.15*salario
    print("Seu antigo salário  é: " ,salario)
    print("O percentual adicionado ao seu salário é: " ,percentual)
    print("Seu novo salário agora é: " ,salario2)
    
elif (salario >= 700 and salario < 1500):
    percentual = 0.10*salario
    salario2 = salario + 0.10*salario
    print("Seu antigo salário  é: " ,salario)
    print("O percentual adicionado ao seu salário é: " ,percentual)
    print("Seu novo salário agora é: " ,salario2)
    
elif (salario >= 1500):
    percentual = 0.05*salario
    salario2 = salario + 0.05*salario
    print("Seu antigo salário  é: " ,salario)
    print("O percentual adicionado ao seu salário é: " ,percentual)
    print("Seu novo salário agora é: " ,salario2)
