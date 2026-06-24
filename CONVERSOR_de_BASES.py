# TODO: Octal para Decimal
# TODO: Octal para Binario
# TODO: Octal para Hexadecimal
# TODO: Hexadecimal para Decimal
# TODO: Hexadecimal para Binario
# TODO: Hexadecimal para Octal

import sys;

def escolha():
    '''
    Pede ao usuário uma opção e chama as funções de acordo com a escolha.
    None -> None
    '''
    escolha: int = 0;
    valor: int = 0;

    while escolha != 13:
        escolha = int(input('Digite o numero de uma das operações: '));
        if escolha == 1:
            valor = int(input('Digite o numero em DECIMAL para ser convertido em BINARIO: '));
            resposta(valor, 2, dec_para_bin(valor));
        elif escolha == 2:
            valor = int(input('Digite o numero em DECIMAL para ser convertido em OCTAL: '));
            resposta(valor, 8, dec_para_oct(valor));
        elif escolha == 3:
            valor = int(input('Digite o numero em DECIMAL para ser convertido em HEXADECIMAL: '));
            resposta(valor, 16, dec_para_hex(valor));
        elif escolha == 4:
            # O input aqui não sera convertido em int pois dentro da função ele sera transformado em uma list.
            valor = input('Digite o numero em BINARIO para ser convertido em DECIMAL: ');
            resposta(valor, 10, bin_para_dec(valor));
        elif escolha == 5:
            # O input aqui não sera convertido em int pois dentro da função ele sera transformado em uma list.
            valor = input('Digite o numero em BINARIO para ser convertido em OCTAL: ');
            resposta(valor, 8, bin_para_oct(valor));
        elif escolha == 6:
            # O input aqui não sera convertido em int pois dentro da função ele sera transformado em uma list.
            valor = input('Digite o numero em BINARIO para ser convertido em HEXADECIMAL: ');
            resposta(valor, 16, bin_para_hex(valor));
    sys.exit();

def dec_para_bin(decimal):
    '''
    Converte um numero DECIMAL em BINARIO e o retorna.
    int -> list
    '''
    resultado = [];
    quociente = decimal;

    while quociente > 0:    
        resultado.append(quociente % 2);
        quociente = quociente // 2;
    resultado = resultado[::-1];
    return resultado;

def dec_para_oct(decimal):
    '''
    Converte um numero DECIMAL em OCTAL e o retorna.
    int -> list
    '''
    resultado = [];
    quociente = decimal;

    while quociente > 0:    
        resultado.append(quociente % 8);
        quociente = quociente // 8;
    resultado = resultado[::-1];
    return resultado;

def dec_para_hex(decimal):
    '''
    Converte um numero DECIMAL em HEXADECIMAL e o retorna.
    int -> list
    '''
    resultado = [];
    quociente = decimal;

    while quociente > 0:    
        resultado.append(str(quociente % 16));
        quociente = quociente // 16;
    resultado = resultado[::-1];
    for i in range(len(resultado)):
        if resultado[i] == '10':
            resultado[i] = 'A';
        elif resultado[i] == '11':
            resultado[i] = 'B';
        elif resultado[i] == '12':
            resultado[i] = 'C';
        elif resultado[i] == '13':
            resultado[i] = 'D';
        elif resultado[i] == '14':
            resultado[i] = 'E';
        elif resultado[i] == '15':
            resultado[i] = 'F';
    return resultado;

def bin_para_dec(binario):
    '''
    Converte um numero BINARIO em DECIMAL e o retorna.
    str -> int
    '''
    numeros_str = list(binario);
    numeros_int = [];
    quantidade = len(numeros_str) - 1;
    resultado: int = 0;
    i: int = 0;

    for num in numeros_str:
        numeros_int.append(int(num));
        resultado = resultado + (numeros_int[i] * (2 ** (quantidade - i)));
        i+=1
    return resultado;

def bin_para_oct(binario):
    '''
    Converte um numero BINARIO em OCTAL e o retorna
    str -> str
    '''
    numeros_str = list(binario);
    tamanho = len(numeros_str);
    bloco: str = '';
    resultado: str = '';

    if tamanho % 3 != 0:
        numeros_str = numeros_str[::-1];
        while tamanho % 3 > 0:
            numeros_str = numeros_str + ['0'];
            tamanho = len(numeros_str);
        numeros_str = numeros_str[::-1];
    for i in range(tamanho):
            bloco = bloco + numeros_str[i];
            if len(bloco) == 3:
                resultado = resultado + str(bin_para_dec(bloco));
                bloco = '';
    return resultado;

def bin_para_hex(binario):
    '''
    Converte um numero BINARIO em HEXADECIMAl e o retorna
    str -> str
    '''
    numeros_str = list(binario);
    tamanho = len(numeros_str);
    bloco: str = '';
    resultado: str = '';

    if tamanho % 4 != 0:
        numeros_str = numeros_str[::-1];
        while tamanho % 4 > 0:
            numeros_str = numeros_str + ['0'];
            tamanho = len(numeros_str);
        numeros_str = numeros_str[::-1];
    for i in range(tamanho):
            bloco = bloco + numeros_str[i];
            if len(bloco) == 4:
                if bloco == '1010':
                    resultado = resultado + 'A';
                elif bloco == '1011':
                    resultado = resultado + 'B';
                elif bloco == '1100':
                    resultado = resultado + 'C';
                elif bloco == '1101':
                    resultado = resultado + 'D';
                elif bloco == '1110':
                    resultado = resultado + 'E';
                elif bloco == '1111':
                    resultado = resultado + 'F';
                else:
                    resultado = resultado + str(bin_para_dec(bloco));
                bloco = '';
    return resultado;

def resposta(numero, base, resultado):
    '''
    Apresenta a resposta formatada de uma conversão. 
    Any, int, list ou Any -> None
    '''
    conversao: str = '';
    saida: str = '';

    if base == 10:
        conversao = 'DECIMAL';
    elif base == 2:
        conversao = 'BINARIO';
    elif base == 8:
        conversao = 'OCTAL';
    elif base == 16:
        conversao = 'HEXADECIMAL';
    if type(resultado) == list:
        for valor in resultado:
            saida = saida + str(valor);
    else:
        saida = str(resultado);
    print(f'{numero} -> {conversao} = {saida}');

def main():
    '''
    Procedimento principal.
    None -> None
    '''
    print('Operações:');
    print('1 - Decimal para Binario');
    print('2 - Decimal para Octal');
    print('3 - Decimal para Hexadecimal');
    print('4 - Binario para Decimal');
    print('5 - Binario para Octal')
    print('6 - Binario para Hexadecimal');
    print('7 - Octal para Decimal');
    print('8 - Octal para Binario');
    print('9 - Octal para Hexadecimal');
    print('10 - Hexadecimal para Decimal');
    print('11 - Hexadecimal para Binario');
    print('12 - Hexadecimal para Octal');
    print('13 - Fechar Programa');
    escolha();
    
if __name__ == '__main__':
    main();
