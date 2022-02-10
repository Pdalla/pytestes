
#Programa Principal
while True:
# Criar Lista de Valores da Loja
    print('=-='*13)
    print('Bem Vindo ao Comparador de Lancamentos')
    print('=-='*13)
    lj = int(input('Digite a quantidade de lancamentos na LOJA:\n'))
    loja=list()
    v = list()
    for c in range(lj):
        if c ==0:
            print('Cole os lancamentos da LOJA')
        a =  str.splitlines(input())
        print(a)
        if a in loja:
            v.append(a)
        else:
            loja.append(a)
        c = c + 1
#Criar Lista de Valores da Retaguarda
    ret = int(input('Quantidade de Lancamentos na RETAGUARDA:\n'))
    retaguarda = list()
    for c in range(ret):
        if c ==0:
            print('Cole os lancamentos da RETAGUARDA')
        b = str.splitlines(input())
        print(b)
        retaguarda.append(b)
        c = c + 1
#Comparador de Loja e Retaguarda
    dif = list()
    for i in range(0,len(loja)):
        if loja[i] not in retaguarda:
            dif.append(loja[i])
        else:
            continue
    dif = dif + v[:]
    print('=-='*13)
    print('Calculando Lancamentos Faltando')
    print('=-='*13)

    print('')
    print('')
    print(f'Os valores que estao faltando na retaguarda sao: \n {dif}')
    r = str(input('Quer continuar [S/N]'))
    if r in 'Nn':
        break
input('Press ENTER to exit')
#while :True
    #  valores.append(n)
