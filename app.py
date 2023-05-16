# PROJETO 7 - PYTONISTA AUTODIDATA - CONVERSOR UNIVERSAL DE MOEDAS

from py_currency_converter import convert


# Funções
def tratar_moeda_inicial(moeda_inicial):
    try:
        if moeda_inicial == '1':
            moeda_inicial = 'USD'

        elif moeda_inicial == '2':
            moeda_inicial = 'BRL'

        elif moeda_inicial == '3':
            moeda_inicial = input('Digite uma moeda(3 dígitos): ')
    
        return moeda_inicial
    except:
        print('Selecione uma moeda válida')


def tratar_moeda_cambio(moeda_cambio):
    try:
        if moeda_cambio == '1':
            moeda_cambio = 'USD'

        elif moeda_cambio == '2':
            moeda_cambio = 'BRL'

        elif moeda_cambio == '3':
            moeda_cambio = input('Digite uma moeda(3 dígitos): ')
        
        return moeda_cambio
    except:
        print('Selecione uma moeda válida')

# Corpo principal

while True:
    try:
        print(43*'-')
        print('BEM-VINDO AO CONVERSOR UNIVERSAL DE MOEDAS\n')

        # Escolha do valor a ser convertido
        valor = float(input('Digite um valor: '))

        while True:
            # Escolha da moeda inicial
            print('\nMOEDAS\n1 - USD\n2 - BRL\n3 - OUTRA')
            converter_de = input('Escolha uma moeda inicial: ')
            if converter_de in ['1','2', '3']: 
                moeda_inicial = tratar_moeda_inicial(converter_de)
                break
            else: 
                print('\nERRO: Selecione somente as opções 1, 2 ou 3')
                

        while True:
            # Escolha da moeda de cambio
            print('\nMOEDA DE CÂMBIO\n1 - USD\n2 - BRL\n3 - OUTRA')
            converter_para = input('Escolha uma moeda de câmbio: ')
            if converter_de in ['1','2', '3']: 
                moeda_cambio = tratar_moeda_cambio(converter_para)
                break
            else: 
                print('\nERRO: Selecione somente as opções 1, 2 ou 3')
        


        # fazendo a conversão
        resultado = convert(base=moeda_inicial, amount=valor, to=[moeda_cambio])

        # Exibindo o resultado
        print('')
        print(f'{valor} {moeda_inicial} - {resultado[moeda_cambio]:.2f} {moeda_cambio}')
    except:
        print('Selecione uma moeda válida')
        break
    
