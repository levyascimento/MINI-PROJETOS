import math 
from time import sleep

print("=-="*20)
print("\033[32mBEM VINDO Á JOIN.PY\033[m")
print("=-="*20)
sleep(1)
def boa(msg):
    print("=-="*20)
    print(f"{msg}")
    print("=-="*20)


while True:
    print("""\033[33mEscolha uma opçao:
    [1] CALCULADORA DIGITAL
    [2] CADRASTRO DE PESSOAS
    [3] LISTA DE COMPRAS
    [4] MINI GAME
    [5] FECHAR APP!\033[m""")

    opcao = int(input("Digite qual á opção desejada: "))
    while opcao not in (1, 2, 3, 4, 5):
        opcao = int(input("\033[31mDigite uma opção valida: \033"))

    if opcao == 1:
        print("\033[35mBEM VINDO SUA CALCULADORA DIGITAL!\033[m")
        num01 = float(input("Digite um numero: "))
        num02 = float(input("Digite outro numero: "))
        print("\033[34mAnalisando numeros....\033[m")
        sleep(1)
        while True:
            print("""\033[33mSelecione uma opção:
        [1] ADIÇÃO
        [2] SUBTRAÇÃO
        [3] MULTIPLICAÇÃO
        [4] DIVISÃO
        [5] RAIZ QUADRADA
        [6] POTENCIA
        [7] REDEFINIR NUMEROS
        [8] ADCIONAR UM NOVO NUMERO (NOT FOUND)\033[m""")
            pergunta = int(input("Digite a opção desejada: "))
            while pergunta not in (1, 2, 3, 4, 5, 6, 7, 8):
                pergunta = int(input("\033[31mDigite uma opção valida: \033[m"))
            if pergunta == 1:
                print(f"\033[32mA soma dos numeros é de {(num01 + num02):.0f}\033[m")
            elif pergunta == 2:
                print(f"\033[32mA subtração dos numeros é de {(num01 - num02):.0f}\033[m")
            elif pergunta == 3:
                print(f"\033[32mA multiplicação dos numeros é de {(num01 * num02):.0f}\033[m")
            elif pergunta == 4:
                per = int(input("\033[36mSelecione [1] para divisão inteira é [2] para divisão comum: \033[m"))
                while per not in (1, 2):
                    print("\033[31mDigite um opção valida!\033[m")
                    per = int(input("\033[36mSelecione [1] para divisão inteira é [2] para divisão comum: \033[m"))
                if per == 1:
                    print(f"\033[32mA divisão inteira dos numeros é de {(num01 // num02):.0f}\033[m")
                elif per == 2:
                    print(f"\033[32mA divisão dos dois numeros é de {(num01 / num02):.2f}\033[m")
            elif pergunta == 5:
                while True:
                    print("""\033[33m   [1] FAZER A RAIZ QUADRADA DE CADA NUMERO
    [2] FAZER A RAIZ QUADRADA DA SOMA DOS DOIS NUMEROS
    [3] FAZER A RAIZ QUADRADA DA SUBTRAÇÃO DOS DOIS NUMEROS
    [4] FAZER A RAIZ QUADRADA DA MULTIPLICAÇÃO DOS DOIS NUMEROS
    [5] FAZER A RAIZ QUADRADA DA DIVISÃO DOS DOIS NUMEROS\033[m""")
                    p = int(input("Digite a opção desejada: "))
                    while p not in (1, 2, 3, 4, 5):
                        print("\033[31mDigite um opção valida!\033[m")
                        p = int(input("\033[36mDigite a opção desejada: \033[m"))
                    if p == 1:
                        primeiro = math.sqrt(num01)
                        segundo = math.sqrt(num02)
                        print(f"\033[32mA raiz qualdrada do primeiro numero é {primeiro:.2f} é a do segundo numero é {segundo:.2f}\033[m")
                    elif p == 2:
                        soma = num01 + num02
                        raizSoma = math.sqrt(soma)
                        print(f"\033[32mO Valor total foi de {raizSoma:.2f}\033[m")
                    elif p == 3:
                        sub = num01 - num02
                        raizSub = math.sqrt(sub)
                        print("\033[32mO valor total foi de {:.2f}\033[m".format(raizSub)) 
                    elif p == 4:
                        mult = num01 * num02
                        raizMult = math.sqrt(mult)
                        print("\033[32mO Valor total foi de {:.2f}\033[m".format(raizMult))
                    elif p == 5:
                        div = num01 // num02
                        raizDiv = math.sqrt(div)
                        print("\033[32mO Valor total foi de {:.2f}\033[m".format(raizDiv))
                    comentRaiz = input("\033[36mQuer tentar novamnete? [S/N]: \033[m").strip().upper()[0]
                    while comentRaiz not in "SN":
                        print("\033[31mDigite um opção valida!\033[m")
                        comentRaiz = input("\033[36mQuer tentar novamente? Digite [S/N]: \033[m").strip().upper()[0]
                    if comentRaiz == "N":
                        break
            elif pergunta == 6:
                while True:
                    print("""\033[33mVeja as opções abaixo:
    [1] POTENCIA DE CADA NUMERO
    [2] POTENCIA DOS NUMEROS SOMADOS
    [3] POTENCIA DOS NUMEROS SUBTRAIDOS\033[m""")
                    perP = int(input("\033[36mDigite o valor elevado ao numero: \033[m"))
                    perguntaPotencia = int(input("\033[36mDigite uma das opções acima: \033[m"))
                    
                    while perguntaPotencia not in (1, 2 ,3):
                        print("\033[31mDigite um valor valido!\033[m")
                        perguntaPotencia = int(input("\033[36mDigite uma das opções acima: \033[m"))
                    if perguntaPotencia == 1:
                        pri = num01**perP
                        segu = num02**perP
                        print(f"\033[32mA potencia do primeiro numero é {pri:.0f} é a potencia do segundo numero é {segu:.0f}\033[m")
                    elif perguntaPotencia == 2:
                        res = (num01 + num02)** perP
                        print(f"\033[32mA potencia dos numeros somados é de {res:.0f}\033[m")
                    elif perguntaPotencia == 3:
                        resul = (num01 - num02)**perP
                        print(f"\033[32mA potencia dos numeros subtraidos é de {resul:.0f}\033[m")
                    comentPotencia = input("\nQuer tentar novamnete? Digite [S/N]: ").upper().strip()[0]
                    while comentPotencia not in "SN":
                        print("\033[31mDigite um opção valida!\033[m")
                        comentPotencia = input("\033[36mQuer tentar novamnete? Digite [S/N]: \033[m").upper().strip()[0]
                    if comentPotencia == "N":
                        break
            elif pergunta == 7:
                num01 = float(input("\033[33mDigite seu primeiro novo numero: \033[m"))
                num02 = float(input("\033[33mDigite seu segundo novo numero: \033[m"))
            print("\nDigite [S] para continuar [N] para mudar de APP")
            perguntaCalcu = input("\033[36mQUER CONTINUAR CALCULANDO OU DESEJA SAIR: \033[m").upper().strip()[0]
            while perguntaCalcu not in "SN":
                print("\033[31mDigite uma opção valida!\033[m")
                perguntaCalcu = input("\033[36mQUER CONTINUAR CALCULANDO OU DESEJA SAIR: \033[m").upper().strip()[0]
            if perguntaCalcu == "N":
                break
    elif opcao == 2:
        dados = list()
        geral = dict()
        listaNome = list()
        listaIdade = list()
        listaSexo = list()
        print("-=-"*20)
        print("\033[35mBEM VINDO AO CADRASTRO DE PESSOAS!\033[m")
        print("-=-"*20)
        sleep(1)
        while True:
            select = input("\033[34mDeseja ver as opções? [S/N]: \033[m").upper().strip()[0]
            while select not in "SN":
                print("\033[31mDIGITE UMA OPÇÃO VALIDA!\033[m")
                select = input("\033[34mDeseja ver as opções? [S/N]: \033[m").upper().strip()[0]
            if select == "N":
                sleep(1)
                break
            elif select == "S":
                print("""\033[33mSelecione um opção:
    [1] CADRASTRA UMA PESSOA
    [2] ALTERAR DADOS DE CADRASTRO
    [3] TOTAL DE PESSOAS CADRASTRADAS
    [4] TOTAL DE PESSOAS +18
    [5] TOTAL DE HOMENS CADRASTRADOS
    [6] TOTAL DE MULHERES CADRASTRADAS\033[m""")
            op = int(input("\033[36mDigite a opção desejada: \033[m"))
            while op not in (1, 2, 3, 4, 5, 6):
                print("\033[31mOpção não encontrada digite uma opção valida\033[m")
                op = int(input("\033[36mDigite a opção desejada: \033[m"))

            if op == 1:
                while True:
                    nome = input("\033[36mDigite o nome da pessoas a ser cadrastra: \033[m").strip().capitalize()
                    idade = int(input(f"\033[36mOlá\033[m \033[31m{nome}\033[m \033[36mDigite sua idade: \033[m"))
                    sexo = input("\033[36multimo dado Digite seu sexo [M/F]: \033[m").strip().upper()[0]
                    while sexo not in "MF":
                        print("\033[31mDigite seu sexo biologico\033[m")
                        sexo = input("ultimo dado Digite seu sexo [M/F]: ").strip().upper()[0]
                    geral["nome"] = nome
                    geral["idade"] = idade
                    geral["sexo"] = sexo
                    listaNome.append(nome)
                    listaIdade.append(idade)
                    listaSexo.append(sexo)
                    dados.append(geral.copy())
                    print(dados)
                    geral.clear()
                    pp = input("\033[32mDeseja cadrastrar outra pessoa? [S/N]: \033[m").upper().strip()[0]
                    while pp not in "SN":
                        print("\033[31mDigite uma opção valida!\033[m")
                        pp = input("\033[32mDeseja cadrastrar outra pessoa? [S/N]: \033[m").upper().strip()[0]
                    if pp == "N":
                        sleep(1)
                        break 
            elif op == 2:
                print("""\033[33mVeja as opções abaixo:
    [1] MUDAR O NOME DO CADRASTRO
    [2] MUDAR IDADE DO CADRASTRO
    [3] MUDAR O SEXO DO CADRASTRO
    [4] REFAZER O CADRASTRO\033[m""")
                cadrastro = int(input("\036[32mDigite a opção desejada: \033[m"))
                if cadrastro == 1:
                    for i, no in enumerate(listaNome):
                        print(f"\033[32mO indice\033[m \033[31m[{i}]\033[m \033[32m=\033[m \033[31m[{no}]\033[m \033[32mCadrastrado\033[m")
                    sleep(1)
                    opc = int(input("\033[36mDigite o indice de acordo com o seu nome: \033[m"))
                    listaNome.pop(opc)
                    listaNome.insert(opc, input("\033[32mDigite seu novo nome: \033[m"))
                elif cadrastro == 2:
                    for i, ida in enumerate(listaIdade):
                        print(f"\033[32mO indice\033[m \033[31m[{i}]\033[m \033[32m=\033[m \033[31m[{ida}\033[m \033[32mCadrastrado]\033[m")
                    sleep(1)
                    opc = int(input("\033[36mDigite o indice de acordo com sua idade: \033[m"))
                    listaIdade.pop(opc)
                    listaIdade.insert(opc, int(input("\033[32mDigite sua nova idade: \033[m")))
                elif cadrastro == 3:
                    for i, no in enumerate(listaNome):
                        print(f"\033[32mO indice\033[m \033[31m[{i}]\033[m \033[32m=\033[m \033[31m[{no}]\033[m \033[32mCadrastrado\033[m", end=" ")
                    sleep(1)
                    opc = int(input("\033[36mDigite o indice de acordo com o seu nome: \033[m"))
                    listaSexo.pop(opc)
                    sexo = input("\033[32mDigite seu novo sexo [M/F]: \033[m").upper().strip()[0]
                    while sexo not in "MF":
                        print("\033[31mDigite um opção valida [M/F]: \033[m")
                        sexo = input("\033[32mDigite seu novo sexo [M/F]: \033[m").upper().strip()[0]
                    listaSexo.insert(opc, sexo)
                elif cadrastro == 4:
                    for i, v in enumerate(listaNome):
                        print(f"\033[32mO indice\033[m \033[31m[{i}]\033[m \033[32mestá cadrastrado:\033[m \033[31m[{v}]\033[m")
                    sleep(1)
                    opc = int(input("\033[36mDigite o indice do seu cadrastro de acordo com o nome: \033[m"))
                    listaNome.pop(opc)
                    listaIdade.pop(opc)
                    listaSexo.pop(opc)
                    nome = input("\033[32mDigite seu novo nome: \033[m").strip().capitalize()
                    idade = int(input(f"\033[32mOlá\033[m \033[31m{nome}\033[m \033[32mDigite sua nova idade: \033[m"))
                    sexo = input("\033[32mDigite seu novo sexo [M/F]: \033[m").strip().upper()[0]
                    while sexo not in "MF":
                        print("\033[31mOpção invalida!\033[m")
                        sexo = input("\033[32mDigite seu novo sexo [M/F]: \033[m").strip().upper()[0]
                    listaNome.insert(opc, nome)
                    listaIdade.insert(opc, idade)
                    listaSexo.insert(opc, sexo)
                    print(listaNome)
                    print("\033[32mCadrastro alterado com sucesso!\033[m")
            elif op == 3:
                print(f"\033[35mO total de pessoas cadrastradas é de\033[m \033[32m{len(listaNome)}\033[m")

            elif op == 4:
                cont = 0
                for i in listaIdade:
                    if i > 18:
                        cont += 1
                print(f"\033[32mO total de pessoas cadrastradas com mais de 18 é de\033[m \033[36m{cont}\033[m")

            elif op == 5:
                homens = 0
                for homem in listaSexo:
                    if homem == "M":
                        homens += 1
                print(f"\033[35mO total de homens cadrastrados é de\033[m \033[32m{homens}\033[m")
            elif op == 6:
                mulheres = 0
                for mulher in listaSexo:
                    if mulher == "F":
                        mulheres += 1
                print(f"\033[35mO total de mulheres cadrastradas é de\033[m \033[32m{mulheres}\033[m")
    elif opcao == 3:
        lista03 = []
        temp = []
        while True:
            print("""\033[33mVeja a lista de opções
    [1] ADICIONAR UM PRODUTO NA LISTA 
    [2] REMOVER UM PRODUTO DA LISTA
    [3] ALTERAR LISTA
    [4] REFAZER LISTA\033[m""")
            
            try:
                opção03 = int(input("\033[36mDigite a opção desejada: \033[m"))
                while opção03 not in (1, 2, 3, 4):
                    print("\033[31mDigite uma opção valida!\033[m")
                    opção03 = int(input("\033[32mDigite uma opção: \033[m"))
            except:
                print("\033[1;31mDigite uma opção valida! Apenas numeros inteiros\033[m")
                sleep(1)
            if opção03 == 1:
                while True:
                    temp.append(input("\033[36mDigite o nome do seu produto: \033[m"))
                    temp.append(float(input(f"\033[36mDigite o valor do produto\033[m \033[31m{temp[0]}: \033[m")))
                    lista03.append(temp[:])
                    temp.clear()
                    print(lista03)
                    per03 = input("\033[36mDeseja colocar mais um produto na lista? [S/N]: \033[m").upper().strip()[0]
                    while per03 not in "SN":
                        print("\033[31mValor não encontrado!\033[m")
                        per03 = input("\033[36mDigite [S] para continuar é [N] para sair!: \033[m").upper().strip()[0]
                    if per03 == "N":
                        break
            elif opção03 == 2:
                while True:
                    for ind, item in enumerate(lista03):
                        print(f"\033[32mNa posição\033[m \033[31m[{ind}]\033[m \033[32mProduto\033[m \033[31m[{item}]\033[m")
                    try:
                        indice03 = int(input("\033[36mDigite o indice do produto á ser removido: \033[m"))
                        lista03.pop(indice03) 
                    except:
                        print(f"\033[1;31mValor não encontrado. Apenas numeros inteiros!\033[m")
                    perg = input("\033[36mDeseja remover mais um produto? [S/N]: \033[m").upper().strip()[0]
                    while perg not in "SN":
                        print("\033[31mDigite um opção valida!\033[m")
                        perg = input("\033[36mDeseja remover mais um produto? [S/N]: \033[m").upper().strip()[0]
                    if perg == "N":
                        print(f"\033[32mSua lista possui\033[m \033[31m[{len(lista03)}]\033[m \033[32mprodutos cadrastrados!\033[m")
                        sleep(1)
                        break
                    
            elif opção03 == 3:
                while True:
                    for ind, ite in enumerate(lista03):
                        print(f"\033[32mNa posição\033[m \033[31m[{ind}]\033[m \033[32mProduto\033[m \033[31m[{ite}]\033[m")
                    try:
                        indec = int(input("\033[36mDigite o indice do valor que deseja alterar: \033[m"))
                        lista03.pop(indec)
                    except:
                        print("\033[31mValor não encontrador\033[m")
                    temp.append(input("\033[32mDigite o nome do seu novo produto: \033[m"))
                    temp.append(float(input(f"\033[32mDigite o valor do seu novo produto\033[m \033[31m{temp}: \033[m")))
                    lista03.insert(indec, temp)
                    temp.clear()
                    ppr = input("\033[36mDeseja alterar mais um produto? [S/N]: \033[m").upper().strip()[0]
                    while ppr not in "SN":
                        print("\033[31mValor não encontrado. Digite um valor valido!\033[m")
                    if ppr == "N":
                        break
            elif opção03 == 4:
                rr = input("\033[35mTem certeza que deseja refazer a lista? [S/N]: \033[m").upper().strip()[0]
                while rr not in "SN":
                    print("\033[31mDigite uma opção valida!\033[m")
                    rr = input("\033[35mTem certeza que deseja refazer a lista? [S/N]: \033[m").upper().strip()[0]
                if rr == "S":
                    lista03.clear()
                    print("\033[32mSua lista está limpa! Digite [1] caso queira adcionar produtos!\033[m")
                else:
                    print("\033[31mLimpeza de lista negada!\033[m")
            pergunta03 = input("\033[36mDeseja continuar [S] ou Sair da lista [N]: \033[m").upper().strip()[0]
            while pergunta03 not in "SN":
                print("\033[31mValor não encontrado! Digite apenas [S/N]\033[m")
                pergunta03 = input("\033[36mDigite [S] para continuar [N] Para sair!: \033[m").upper().strip()[0]
    elif opcao == 4:
        from random import randint as r
        boa("\033[34mBEM VINDO AO MINI GAME (ACERTE O NUMERO)\033[m")
        sleep(1)
        numeros = list()
        while True:
            print("\033[35mPara começar digite um numero de 1 a 50!\033[m")
            try:
                num = int(input("\033[36mDigite um numero de 1 á 50: \033[m"))
                while num > 50:
                    print("\033[31mDigite um numero menor que 50!\033[m")
                    num = int(input("\033[36mDigite um numero de 1 á 50: \033[m"))
            except:
                print("\033[1;31mApenas numeros inteiros! (nada de letras)\033[m")
            n = r(1, 51)
            resul = n + num
            respo = 0
            contador = 0 
            while respo != resul:
                try:
                    respo = int(input(f"\033[36mAgora tente acertar o numero pensado pela maquina : \033[m"))
                    contador += 1
                    numeros.append(respo)
                    if numeros.count(respo) > 1:
                        contador -= 1
                        print("\033[31mVocê já digitou esse numero! Não sera contado como tentativa.\033[m")
                    elif respo > resul:
                        print("\033[32mO Valor digitado é\033[m \033[34mMAIOR\033[m \033[32mque o valor sorteado!\033[m")
                    elif respo < resul:
                        print("\033[32mO Valor digitado é\033[m \033[34mMENOR\033[m \033[32mque o valor sorteado!\033[m")
                except:
                    print("\033[1;31mApenas numeros inteiros! (nada de letras)")
            print(f"\033[34mParabéns você acertou com\033[m \033[31m{contador}\033[m \033[34mTentativas!\033[m")
            numeros.clear()
            perguntaMini = input("\033[36mQuer jogar novamente? [S/N]: \033[m").upper().strip()[0]
            while perguntaMini not in "SN":
                print("\033[31mDigite um valor valido!\033[m")
                perguntaMini = input("\033[36mQuer jogar novamente? [S/N]: \033[m").upper().strip()[0]
            if perguntaMini == "N":
                sleep(1)
                break
    else:
        print("\033[37mGostou do programa? Deixe seu FeedBack Abaixo!\033[m")
        nota = float(input("Nota de 0 á 10: "))
        if nota <= 5:
            print("\033[1;37mVlw pelo mal FeedBack Espero que não volte mais!\033[m")
        else:
            print("\033[1;35mObrigado! Volte sempre.\033[m")
    if opcao == 5:
         break
        