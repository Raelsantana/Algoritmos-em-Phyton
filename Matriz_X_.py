vetor = []

#Dimensões da imagem
dim = 30

i = 0
j = 0

#Formando a matriz com espaços vazios
while i < dim:
    vetor.append([])
    j = 0
    while j < dim:
        vetor[i].append(' ')
        j += 1
    i += 1
i = 0
j = 0

#preenchendo a Diagonal com '#'
while i < dim:
    j = 0
    while j < dim:
        if i == j:
            vetor[i][j] = '#'
        if i == 0:
            vetor[i][j] = '#'
        if j == 0:
            vetor[i][j] = '#'
        if j == (dim - 1):
            vetor[i][j] = '#'

        j += 1
    i += 1

j = 0
i = 0

#Inverte a diagonal
vetor.reverse()
#Preenche novamente a diagonal
while i < dim:
    j = 0
    while j < dim:
        if i == j:
            vetor[i][j] = '#'
        if i == 0:
            vetor[i][j] = '#'

        j += 1
    i += 1


for linha in vetor:
    for elemento in linha:
        print(elemento, end=' ')
    print()




