
#aula de sets

#sets não têm ordem definida
#sets não possuem elementos repetidos
#add (adiciona), update (atualiza e adiciona, itera sobre argumento), clear, discard
#union | (une dois conjuntos / sets)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 3, 4, 5, 7}

# s3 = s1 | s2
# s3 = s1 & s2
# s3 = s1 - s2
s3 = s1 ^ s2

print(s3)


l1 = [1, 2, 3, 3, 3, 4, 4, 'Luiz', 'Luiz']
l1 = set(l1)
l1 = list(l1)

print(l1)