def contar_caracteres(string):
    # um dicionário vazio 'contador' para armazenar as contagens de caracteres:
    contador = dict();
    # itera a string para pegar letra por letra da palavra
    for char in string:
        if char in contador:
            contador[char] += 1;
        else:
            contador[char] = 1;
    # 'if char in contador' se a letra estiver dentro do contador, adicione mais 1 ao valor da chave, caso não, atribui um valor inicial 1
    
    return contador;

entrada = input();
resultado = contar_caracteres(entrada);
print(resultado);

# ex de entrada: abacaxi
# ex de saida: {'a': 3, 'b': 1, 'c': 1, 'x': 1, 'i': 1}