#input da string
#entrada = input("informe uma string: ")

#comanda a função para verificar
#teste_verefi_string(entrada)

def teste_verefi_string(texto):
  #deixa o texto em minúsculo para otimizar a contagem
  texto = texto.lower()

  #contador da letra a
  contador = texto.count('a')

  #verefica se a letra a está na string e mostra o resultado
  if contador > 0:
    print(f"A letra (A) aparece {contador} vezes na string")
  else:
    print(f"A letra (A) não aparece na string")

#input da string
entrada = input("informe uma string: ")

#comanda a função para verificar
teste_verefi_string(entrada)

#fim do código
