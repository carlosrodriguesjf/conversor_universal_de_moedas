# PROJETO 7 - PYTONISTA AUTODIDATA - CONVERSOR UNIVERSAL DE MOEDAS

from py_currency_converter import convert



def tratar_moeda_inicial(moeda_inicial):
        
    if moeda_inicial == '1':
        moeda_inicial = 'USD'

    elif moeda_inicial == '2':
        moeda_inicial = 'BRL'

    elif moeda_inicial == '3':
        moeda_inicial = input('Digite uma moeda(3 dígitos): ')
  
    return moeda_inicial




def tratar_moeda_cambio(moeda_cambio):
    if moeda_cambio == '1':
        moeda_cambio = 'USD'

    elif moeda_cambio == '2':
        moeda_cambio = 'BRL'

    elif moeda_cambio == '3':
        moeda_cambio = input('Digite uma moeda(3 dígitos): ')
    
    return moeda_cambio



print(43*'-')
print('BEM-VINDO AO CONVERSOR UNIVERSAL DE MOEDAS\n')

# Escolha do valor a ser convertido
valor = float(input('Digite um valor: '))

# Escolha da moeda inicial

print('\nMOEDAS\n1 - USD\n2 - BRL\n3 - OUTRA')
converter_de = input('Escolha uma moeda inicial: ')
moeda_inicial = tratar_moeda_inicial(converter_de)


# Escolha da moeda de cambio
print('\nMOEDA DE CÂMBIO\n1 - USD\n2 - BRL\n3 - OUTRA')
converter_para = input('Escolha uma moeda de câmbio: ')
moeda_cambio = tratar_moeda_cambio(converter_para)


# fazendo a conversão
resultado = convert(base=moeda_inicial, amount=valor, to=[moeda_cambio])


print('')
print(f'{valor} {moeda_inicial} - {resultado[moeda_cambio]} {moeda_cambio}')
    
