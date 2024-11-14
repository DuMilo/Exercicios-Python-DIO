
# função que soma todos os elementos da tupla 
def soma_tupla(tupla):
    return sum(tupla);

# essa condição só funciona neste arquivo, ao importar esse código para outro código
# apenas as funções vao poder ser utilizadas mas o "if" não será inicializado.
if __name__ == "__main__":
    lista_strings = input();
    
    elementos = tuple(map(int, lista_strings.split()));
    # split = divide os elementos dados em lista_string, ex: 10 20 30 após split fica ["10","20","30"]
    # map() é uma função que aplica funções a cada elemento de uma coleção, 
    # nesse caso ele aplicou int() a tupla para tornar os elementos como números inteiros.
    # tuple certifica que elementos está recebendo uma tupla
    
    resultado = soma_tupla(elementos);
    print(f"A soma dos elementos da tupla é: {resultado}");