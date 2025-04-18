menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair'''

saldo = 0
limite = 500
extrato = []
numero_de_saques = 0
LIMITE_SAQUES = 3

def depositar (valor):
    if valor > 0:
        global saldo
        saldo += valor
        extrato.append(f'Depósito de R$ {valor:.2f}')
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
    else:
        print('Valor inválido para depósito.')

def sacar (valor_saque):
    global saldo, numero_de_saques, extrato, LIMITE_SAQUES
    if saldo >= valor_saque <= limite and numero_de_saques < LIMITE_SAQUES:
        saldo -= valor_saque
        extrato.append(f'Saque de R$ {valor_saque:.2f}')
        print(f'Saldo atual: R$ {saldo:.2f}')
        print(f'Saque de R$ {valor_saque:.2f} realizado com sucesso!')
        numero_de_saques += 1
    
    elif numero_de_saques >= LIMITE_SAQUES:
        print('Número máximo de saques atingido!')

    elif valor_saque > saldo:
        print('Saldo insuficiente!')
    
    else:
        print('Valor inválido para saque!')

def ver_extrato ():
    if extrato == []:
        print('Não foram realizadas movimentações.')
    else:
        print('Extrato:')
        for item in extrato:
            print(item)
    print(f'Saldo: R$ {saldo:.2f}')

while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input('Informe o valor do depósito: R$ '))
        depositar(valor)

    elif opcao == '2':
        valor = float(input('Informe o valor do saque: R$ '))
        sacar(valor)

    elif opcao == '3':
        ver_extrato()

    elif opcao == '0':
        print('Obrigado por usar nosso sistema!')
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')