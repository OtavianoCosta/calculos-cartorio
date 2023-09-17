print("programa para calcular o servico")
print("(1)autenticações (2)Sem valor (3)Com Valor (4)Autenticidade")
escolha = int(input("Qual Serviço voce quer saber?"))

if (escolha == 1):
    servico = int(input("Digite a quantidade"))
    aut = servico * 4.40
    print("O cliente vai gastar R${} Reais".format(aut))
    xerox = input("Teve xerox?")
    xerox = xerox.upper()
    if (xerox == "SIM"):
        xeroxx = float(input("Qual foi a quantidade?"))
        xeroxx = xeroxx * 0.75
        print("Com as xerox o seu Clinte vai gastar    R${}".format(xeroxx + aut))
    else:
        print("Entao cliente vai gastar R${} Reais".format(aut))


elif (escolha == 2):
    servico = int(input("Digite a quantidade"))
    semva = servico * 7.58
    print("O cliente vai gastar R${}Reais".format(semva))
    xerox = input("Teve xerox?")
    xerox = xerox.upper()
    if (xerox == "SIM"):
        xeroxx = float(input("Qual foi a quantidade?"))
        xeroxx = xeroxx * 0.75
        print("Com as xerox o seu Clinte vai gastar    R${}".format(xeroxx + semva))
    else:
        print("Entao cliente vai gastar R${} Reais".format(semva))

elif (escolha == 3):
    servico = int(input("Digite a quantidade"))
    comva = servico * 11.59
    print("O cliente vai gastar R${} Reais".format(comva))
    xerox = input("Teve xerox?")
    xerox = xerox.upper()
    if (xerox == "SIM"):
        xeroxx = float(input("Qual foi a quantidade?"))
        xeroxx = xeroxx * 0.75
        print("Com as xerox o seu Clinte vai gastar    R${}".format(xeroxx + comva))
    else:
        print("Entao cliente vai gastar R${} Reais".format(comva))

else:
    servico = int(input("Digite a quantidade"))
    verd = servico * 19.40
    print("O cliente vai gastar R${} Reais".format(verd))
    xerox = input("Teve xerox?")
    xerox = xerox.upper()
    if (xerox == "SIM"):
        xeroxx = float(input("Qual foi a quantidade?"))
        xeroxx = xeroxx * 0.75
        print("Com as xerox o seu Clinte vai gastar    R${}".format(xeroxx + verd))
    else:
        print("Entao cliente vai gastar R${} Reais".format(verd))

input("Servico Finalizado!!")