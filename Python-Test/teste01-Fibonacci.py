def teste_fibonacci(F):

  #Começa os primeiros números da sequência:
  a, b = 0, 1

  #Seguintes comandos abaixo da inicio a sequência de fibonacci até que o valor seja maior ou igual a N:
  while a <= F:
    if a == F:
        return True
    a, b = b, a + b
  return False
  
#Input do número logo abaixo:
num =  int(input("Digite um número para verificar se ele pertence a sequência de Fibonacci: "))

#Análise para ver se o número condiz com a sequência:
if teste_fibonacci(num):
   print(f"O número {num} pertence à sequência!")
else:
   print(f"O número {num} não pertence à sequência!")
  
  #fim do código