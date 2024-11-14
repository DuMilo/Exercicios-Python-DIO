# função para achar elementos em comum
def elementos_comuns(lista1, lista2):
    set1 = set(map(int, lista1));
    set2 = set(map(int, lista2));
    # transforma em conjunto(set) pois apenas conjuntos suportam o metodo intersection()
    
    return list(set1.intersection(set2));
    # depois transforma em lista igual o exercicio pede

# leitura das listas
# separa antes de entrar na função para passar pelo metodo split()
lista1 = input().split();
lista2 = input().split();

# verifica se todos (all) os elementos das listas podem ser convertidos para inteiros (se são digitos)
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2);
    print(f"Elementos comuns às duas listas: {comuns}");
else:
    print("Entrada inválida.");