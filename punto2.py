numeros=[5,6,58,8,12,12,25]
def mayor(numeros):
    maximo=numeros[0];
    for i in numeros:
     if i > maximo:
        maximo=i
    return maximo

def menor(numeros):
    minimo=numeros[0];
    for i in numeros:
     if i < minimo:
        minimo=i
    return minimo

def numero(numeros):
 print("El valor maximo es",max(numeros))
 print("El valor minimo es",min(numeros))
numero(numeros)