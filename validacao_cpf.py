
def verif_dig(): #Função resposável pelo calculo de validação do cpf.

    #Recebe o CPF do usuário, divide em uma lista de strings com a função split, e em seguida transforma em inteiros.
    valid = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    entrada_cpf = input("Digite o seu CPF:")
    entrada_cpf.split()
    cpf = list(map(int,entrada_cpf))
    quant_itens = len(cpf)

    if quant_itens < 11:
        print("Dados insuficientes.")
        return 0
    elif quant_itens > 11:
        print("Número digitado não suportado.")
        return 0

    #Separa os dois ultimos dígitos removidos da lista cpf digitada pelo usuário dentro da variável dig_remov.
    dig_remov = []
    dig_remov.append(cpf.pop())
    dig_remov.append(cpf.pop())
    dig_remov.reverse()


    #Multiplicação da lista valid pela lista que contém os números do cpf, agrupando na lista prim_dig.
    prim_dig = [a * b for a, b in zip(cpf, valid)]

    #Função sum para somar todos os índices da lista prim_dig.
    soma_prim_dig = sum(prim_dig)

    #Dividindo a soma dos índices por 11, e calculando o resto da divisão.
    prim_dig = (soma_prim_dig / 11) #14,7272
    resto = (soma_prim_dig % 11)

    #validação
    if resto < 2:
        prim_dig = 0
    elif resto >= 2:
        prim_dig = (11 - resto)

    #adicionando o primeiro número encontrado a lista principal do cpf.
    cpf.append(prim_dig)
    valid.insert(0, 11)

    #Repetindo o cálculo para encontrar o segundo digito.
    segundo_dig = [a * b for a, b in zip(cpf, valid)]

    soma_segundo_dig = sum(segundo_dig) #204

    segundo_dig = (soma_segundo_dig / 11)
    resto_2 = (soma_segundo_dig % 11)
    #validação
    if resto_2 < 2:
        segundo_dig = 0
    elif resto_2 >= 2:
        segundo_dig = (11 - resto_2)

    #Adiciona os dois ultimos digitos dentro da variável cpf.
    cpf.append(segundo_dig)

    #remove os dois ultimos digitos encontrados e adiciona na vista valid_cpf.
    valid_cpf = []
    valid_cpf.append(cpf.pop())
    valid_cpf.append(cpf.pop())
    valid_cpf.reverse()

    #Faz a comparação entre os numeros digitados pelo usuário e os encontrados pelo algoritmo.
    if dig_remov == valid_cpf:
        print("Seu CPF é válido.")
    else:
        print("CPF inválido.")


# :)

verif_dig()





