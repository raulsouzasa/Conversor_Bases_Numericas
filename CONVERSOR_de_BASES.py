import sys;

def decimal_para_binario(decimal):
    resultado = [];
    quociente = decimal;

    while quociente > 0:    
        resultado.append(quociente % 2);
        quociente = quociente // 2
    resultado = resultado[::-1];
    print(resultado);
    
def binario_para_decimal(binario):
    numeros_str = list(binario);
    numeros_int = [];
    quantidade = len(numeros_str) - 1;
    resultado: int = 0;
    i: int = 0;

    for num in numeros_str:
        numeros_int.append(int(num));
        resultado = resultado + (numeros_int[i] * (2 ** (quantidade - i)));
        i+=1
    print(resultado);

def main():
    escolha: int = 0;
    numero: int = 0;

    while escolha != 3:
        print('Operações:');
        print('1 - Decimal para Binario');
        print('2 - Binario para Decimal');
        print('3 - Fechar Programa');
        escolha = int(input('Digite o numero de uma das operações: '));
        if escolha == 1:
            numero = int(input('Digite o numero em DECIMAL para ser convertido em BINARIO: '));
            decimal_para_binario(numero);
        if escolha == 2:
            numero = input('Digite o numero em BINARIO para ser convertido em DECIMAL: ');
            binario_para_decimal(numero);
    sys.exit();
    
if __name__ == '__main__':
    main();
