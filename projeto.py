from tkinter import *
import sqlite3
from tkinter.ttk import Combobox

database1 = sqlite3.connect('databankpy.db')
cursor1 = database1.cursor()

cursor1.execute ("CREATE TABLE IF NOT EXISTS produtos (nome text, preco integer, estoque integer)")

def Tabelas():
    rootI = Tk()
    rootI.geometry("500x200")

    def NomeprodutosGet():
        listaFinal = []
        cursor1.execute('''SELECT * from produtos''')
        produtosmatriz = cursor1.fetchall()
        for linha in produtosmatriz:
            prodName = linha[0]
            listaFinal.append(prodName)
        return listaFinal

    def ValorprodutosGet():
        listaFinal = []
        cursor1.execute('''SELECT * from produtos''')
        produtosmatriz = cursor1.fetchall()
        for linha in produtosmatriz:
            prodName = linha[1]
            listaFinal.append(prodName)
        return listaFinal

    def StockprodutosGet():
        listaFinal = []
        cursor1.execute('''SELECT * from produtos''')
        produtosmatriz = cursor1.fetchall()
        for linha in produtosmatriz:
            prodName = linha[2]
            listaFinal.append(prodName)
        return listaFinal
    
    produtos_list = NomeprodutosGet()
    valores_list = ValorprodutosGet()
    estoque_list = StockprodutosGet()

    prodListBox = Listbox(rootI,height = 5,bd=3)
    prodListBox.place(relx = 0.1, rely = 0.20)
    for i in produtos_list:
        prodListBox.insert(END,i)

    ValorListBox = Listbox(rootI,height = 5,bd=3)
    ValorListBox.place(relx = 0.4, rely = 0.20)
    for i in valores_list:
        ValorListBox.insert(END,i)

    stockListBox = Listbox(rootI,height = 5,bd=3)
    stockListBox.place(relx = 0.7, rely = 0.20)
    for i in estoque_list:
        stockListBox.insert(END,i)

    precoLabel = Label(rootI,text = "tabela de produtos")
    precoLabel.place(relx = 0.1, rely = 0.10)

    valorLabel = Label(rootI,text = "tabela de valores")
    valorLabel.place(relx = 0.4, rely = 0.10)

    stockLabel = Label(rootI,text = "tabela de estoques")
    stockLabel.place(relx = 0.7, rely = 0.10)

    rootI.mainloop


def ProdutoIndividual():
    rootH = Tk()
    rootH.geometry("400x300")

    def NomeprodutosGet():
        listaFinal = []
        cursor1.execute('''SELECT * from produtos''')
        produtosmatriz = cursor1.fetchall()
        for linha in produtosmatriz:
            prodName = linha[0]
            listaFinal.append(prodName)
        return listaFinal

    def changeStock():
        produto = produtoCombobox.get()
        try:
            novoEstoque = int(stockEntry.get())
            if novoEstoque < 0:
                statusLabel5["text"] = "Valor deve ser no mínimo 0"
            else:
                novoEstoque = str(novoEstoque)
                cursor1.execute(" UPDATE produtos SET estoque = '"+novoEstoque+"' WHERE nome = '"+produto+"' ")
                database1.commit()
                statusLabel5["text"] = "Novo estoque adicionado"
        except ValueError:
            statusLabel5["text"] = "Número inválido"

    def changeValue():
        produto = produtoCombobox.get()
        try:
            preco = float(precoEntry.get())
            if preco <= 0:
                statusLabel5["text"] = "Valor deve ser acima de 0"
            else:
                preco = str(preco)
                cursor1.execute(" UPDATE produtos SET preco = '"+preco+"' WHERE nome = '"+produto+"' ")
                database1.commit()
                statusLabel5["text"] = "Novo valor adicionado"
        except ValueError:
            statusLabel5["text"] = "Número inválido"


    def erase():
        produto = produtoCombobox.get()
        cursor1.execute(" DELETE FROM produtos WHERE nome = '"+produto+"' ")
        database1.commit()
        statusLabel5["text"] = "Mercadoria apagada"

    produtos_list = NomeprodutosGet()

    pageLabel = Label(rootH,text = "Edite o estoque e preços")
    pageLabel.place(relx = 0.3, rely = 0.03)

    produtoLabel = Label(rootH,text = "Escolha um produto:")
    produtoLabel.place(relx = 0.1, rely = 0.13)

    produtoCombobox = Combobox(rootH,values = produtos_list)
    produtoCombobox.place(relx = 0.5, rely = 0.13)

    precoLabel = Label(rootH,text = "digite o novo preço:")
    precoLabel.place(relx = 0.1, rely = 0.23)

    precoEntry = Entry(rootH)
    precoEntry.place(relx = 0.1, rely = 0.33)

    stockLabel = Label(rootH,text = "digite o novo estoque:")
    stockLabel.place(relx = 0.1, rely = 0.43)

    stockEntry = Entry(rootH)
    stockEntry.place(relx = 0.1, rely = 0.53)

    confirmChange = Button(rootH,text = "Mudar preço", command = changeValue)
    confirmChange.place(relx = 0.1, rely = 0.62)

    tablesButton = Button(rootH,text = "Mudar estoque", command = changeStock)
    tablesButton.place(relx = 0.1, rely = 0.70)

    eraseButton = Button(rootH,text = "Apagar mercadoria", command = erase)
    eraseButton.place(relx = 0.1, rely = 0.78)

    tablePage = Button(rootH,text = "tabelas", command = Tabelas)
    tablePage.place(relx = 0.8, rely = 0.78)


    statusLabel5 = Label(rootH,text = "")
    statusLabel5.place(relx = 0.1, rely = 0.90)

    rootH.mainloop


# login do mercado
def mercadologin():
    rootE = Tk()
    rootE.title = "mercado"
    rootE.geometry("400x200")
    
    # página do mercado
    def mercado():
        cursor1.execute('''SELECT * from credenciais''')
        result = cursor1.fetchall()

        email_input = emailmerEntry.get()
        senha_input = passmerEntry.get()
        valor = False
        for linha in result:
            for coluna in linha:
                if coluna == email_input:
                    nome = linha[0]
                    if senha_input == linha[2]:
                        valor = True
                        status = linha[3]
                        statusLabel2["text"] = "logado como %s" %nome
                    elif senha_input != linha[2]:
                        valor = True
                        statusLabel2["text"] = "email ou senha incorretos"
        if valor == False:
            statusLabel2["text"] = "email ou senha incorretos"
        elif status == "empregado":
            # empregado
            rootF = Tk()
            rootF.geometry("400x200")

            # adição de produto
            def AddProd():
                value1 = True
                value2 = True
                nomeProd = nomeProduto.get()

                if nomeProd == "":
                    statusLabel3["text"] = "insira um nome para o produto"
                else:
                    try:
                        precoProd = float(precoProduto.get())
                        quantProd = int(quantidadeProduto.get())

                        precoProd = precoProduto.get()
                        quantProd = quantidadeProduto.get()
                        cursor1.execute("INSERT INTO produtos VALUES ('"+nomeProd+"','"+precoProd+"','"+quantProd+"')")
                        database1.commit()
                        statusLabel3["text"] = "produto %s adicionado"%nomeProd
                    except ValueError:
                        statusLabel3["text"] = "insira um preço e uma quantia válida"
                    
                
                


            empregadoTitle = Label(rootF,text = "Adição de produtos")
            empregadoTitle.place(relx = 0.35, rely = 0.03)

            nomeProdutoLabel = Label(rootF,text = "digite o nome de um produto:")
            nomeProdutoLabel.place(relx = 0.1, rely = 0.18)

            nomeProduto = Entry(rootF)
            nomeProduto.place(relx = 0.6, rely = 0.18)

            precoProdutoLabel = Label(rootF,text = "digite o preço do produto:")
            precoProdutoLabel.place(relx = 0.1, rely = 0.33)

            precoProduto = Entry(rootF)
            precoProduto.place(relx = 0.6, rely = 0.33)

            quantidadeProdutoLabel = Label(rootF,text = "digite uma quantia de estoque:")
            quantidadeProdutoLabel.place(relx = 0.1, rely = 0.48)

            quantidadeProduto = Entry(rootF)
            quantidadeProduto.place(relx = 0.6, rely = 0.48)

            confirmarButton1 = Button(rootF,text = "Confirmar", command = AddProd)
            confirmarButton1.place(relx = 0.4, rely = 0.63)

            statusLabel3 = Label(rootF,text ="")
            statusLabel3.place(relx = 0.1, rely = 0.78)

            nextPageButton = Button(rootF,text= "editar ->", command = ProdutoIndividual)
            nextPageButton.place(relx = 0.7, rely = 0.63)

            rootF.mainloop
        elif status == "consumidor":
            # consumidor
            rootG = Tk()
            rootG.geometry("400x200")

            produtos_list = []

            def produtosGet():
                listaFinal = []
                cursor1.execute('''SELECT * from produtos''')
                produtosmatriz = cursor1.fetchall()
                for linha in produtosmatriz:
                    prodName = linha[0]
                    listaFinal.append(prodName)
                return listaFinal
            # compra de produtos
            def BuyProd():
                value1 = True
                try:
                    quantidade = int(consQuantidade.get())
                except:
                    statusLabel4["text"] = "insira uma quantidade válida"
                    value1 = False
                if value1 == True:
                    nomeProduto = consProdutos.get()
                    email = emailmerEntry.get()
                    quantidade = int(consQuantidade.get())

                    cursor1.execute('''SELECT * from credenciais''')
                    credenciaisMatriz = cursor1.fetchall()
                    for linha in credenciaisMatriz:
                        for coluna in linha:
                            if coluna == email:
                                dinheiroUser = linha[4] # meu dinheiro
                    cursor1.execute('''SELECT * from produtos''')
                    produtosMatriz = cursor1.fetchall()
                    for linha in produtosMatriz:
                        for coluna in linha:
                            if coluna == nomeProduto:
                                precoProduto = linha[1] #preço do produto
                                estoque = linha[2] # quantidade do produto
                    
                    precoFinal = precoProduto * quantidade
                    novoDinheiroUser = dinheiroUser - precoFinal
                    if novoDinheiroUser < 0:
                        statusLabel4["text"] = "fundo monetário insuficiente para finalizar a compra!"
                    elif quantidade > estoque:
                        statusLabel4["text"] = "estoque do produto insuficiente!"
                    else:
                        novoDinheiroUser = str(novoDinheiroUser)
                        novoEstoque = estoque - quantidade
                        novoEstoque = str(novoEstoque)
                        cursor1.execute(" UPDATE credenciais SET dinheiros = '"+novoDinheiroUser+"' WHERE email = '"+email+"' ")
                        cursor1.execute(" UPDATE produtos SET estoque = '"+novoEstoque+"' WHERE nome = '"+nomeProduto+"' ")
                        database1.commit()
                        statusLabel4["text"] = "compra finalizada com sucesso!"
                        saldoUpdateLabel["text"] = "saldo atual de: %s reais"%novoDinheiroUser


            def moneyUpdate():
                email = emailmerEntry.get()
                cursor1.execute('''SELECT * from credenciais''')
                credenciaisMatriz = cursor1.fetchall()
                for linha in credenciaisMatriz:
                    for coluna in linha:
                        if coluna == email:
                            dinheiroUser = linha[4]
                return dinheiroUser

            produtos_list = produtosGet()

            saldo_atual_inicial = moneyUpdate()

            consProdutosLabel = Label(rootG,text = "escolha um produto:")
            consProdutosLabel.place(relx = 0.1, rely = 0.03)

            consQuantidadeLabel = Label(rootG,text = "digite uma quantidade:")
            consQuantidadeLabel.place(relx = 0.1, rely = 0.18)

            consProdutos = Combobox(rootG,values = produtos_list)
            consProdutos.place(relx = 0.6, rely = 0.03)

            consQuantidade = Entry(rootG)
            consQuantidade.place(relx = 0.1, rely = 0.33)

            saldoUpdateLabel = Label(rootG,text = "saldo atual de: %s reais"%saldo_atual_inicial)
            saldoUpdateLabel.place(relx = 0.1, rely = 0.48)

            confirmarButton2 = Button(rootG,text = "Confirmar", command = BuyProd)
            confirmarButton2.place(relx = 0.1, rely = 0.63)

            tabelasButton = Button(rootG,text = "Tabelas", command = Tabelas)
            tabelasButton.place(relx = 0.3, rely = 0.63)

            statusLabel4 = Label(rootG, text = "")
            statusLabel4.place(relx = 0.1, rely = 0.78)

            rootG.mainloop

    mercLoginTilte = Label(rootE,text = "Log-in para o mercado")
    mercLoginTilte.place(relx = 0.4,rely = 0.03)

    emailmerLabel = Label(rootE,text = "Digite seu email:")
    emailmerLabel.place(relx = 0.1,rely = 0.18)

    emailmerEntry = Entry(rootE)
    emailmerEntry.place(relx = 0.4,rely = 0.18)

    passmerLabel = Label(rootE,text = "Digite sua senha:")
    passmerLabel.place(relx = 0.1,rely = 0.33)

    passmerEntry = Entry(rootE,show = "*")
    passmerEntry.place(relx = 0.4,rely = 0.33)

    confirmmerButton = Button(rootE,text = "confirmar", command = mercado)
    confirmmerButton.place(relx = 0.4,rely = 0.48)

    statusLabel2 = Label(rootE,text = "")
    statusLabel2.place(relx = 0.1 ,rely = 0.63)
    
    backButton = Button(rootE,text = "voltar", command = inicio)
    backButton.place(relx = 0,rely = 0)

    rootE.mainloop



def banco():
    rootD = Tk()
    rootD.title = "caixa eletrônico"
    rootD.geometry("400x300")

    def AddMoney():
        cursor1.execute('''SELECT * from credenciais''')
        credenciaisMatriz = cursor1.fetchall()

        email = emailatmEntry.get()
        password = passatmEntry.get()
        moneyToAdd = moneyaddEntry.get()
        moneyToAdd = float(moneyToAdd)
        valor = False
        for linha in credenciaisMatriz:
            for coluna in linha:
                if coluna == email:
                    if password == linha[2]:
                        userMoney = linha[4]
                        userMoney = float(userMoney)
                        newUserMoney = userMoney + moneyToAdd
                        newUserMoney = str(newUserMoney)
                        valor = True
                        cursor1.execute(" UPDATE credenciais SET dinheiros = '"+newUserMoney+"' WHERE email = '"+email+"' ")
                        database1.commit()

                        moneyUpdateLabel["text"] = "novo saldo de %s reais" %newUserMoney
                        statusLabel4["text"] = "transação aceita!"
                    elif password != linha[2]:
                        valor = True
                        moneyUpdateLabel["text"] = ""
                        statusLabel4["text"] = "email ou senha incorretos"
        if valor == False:
            moneyUpdateLabel["text"] = ""
            statusLabel4["text"] = "email ou senha incorretos"

    atmLabel = Label(rootD,text = "Caixa eletrônico")
    atmLabel.place(relx = 0.4,rely = 0.03)

    emailatmLabel = Label(rootD,text = "Digite seu email:")
    emailatmLabel.place(relx = 0.1,rely = 0.18)

    emailatmEntry = Entry(rootD)
    emailatmEntry.place(relx = 0.5,rely = 0.18)

    passatmLabel = Label(rootD,text = "Digite sua senha:")
    passatmLabel.place(relx = 0.1,rely = 0.33)

    passatmEntry = Entry(rootD,show = "*")
    passatmEntry.place(relx = 0.5,rely = 0.33)

    moneyLabel = Label(rootD,text ="Quantia a ser adicionada:")
    moneyLabel.place(relx = 0.1,rely = 0.48)

    moneyaddEntry = Entry(rootD)
    moneyaddEntry.place(relx = 0.5,rely = 0.48)

    enteratmButton = Button(rootD,text = "confirmar", command = AddMoney)
    enteratmButton.place(relx = 0.4,rely = 0.63)

    statusLabel4 = Label(rootD,text ="")
    statusLabel4.place(relx = 0.1,rely = 0.78)

    moneyUpdateLabel = Label(rootD,text = "")
    moneyUpdateLabel.place(relx = 0.1,rely = 0.85)

    backButton = Button(rootD,text = "voltar", command = inicio)
    backButton.place(relx = 0,rely = 0)

    rootD.mainloop





def opensignin():
    rootB = Tk()
    rootB.title = "Log-in"
    rootB.geometry("400x400")
    
    escolha = IntVar()
    escolha.set(1)
    
    def assinar():
        nome = nameEntry.get()
        email = emailEntry.get()
        senha1 = password1Entry.get()
        senha2 = password2Entry.get()
        posic = escolha.get()
        if nome == "" or email == "" or senha1 == "" or senha2 == "":
            statusLabel["text"] = "preencha todos os espaços"
        elif senha1 != senha2:
            statusLabel["text"] = "as senhas são diferentes"
        elif email == senha1:
            statusLabel["text"] = "senha e email devem ser diferentes"
        elif posic == 0:
            cursor1.execute ("CREATE TABLE IF NOT EXISTS credenciais (nome text, email text, senha text, posição text, dinheiros integer)")
            cursor1.execute("INSERT INTO credenciais VALUES ('"+nome+"','"+email+"','"+senha1+"','empregado','00')")
            database1.commit()
            statusLabel["text"] = "credenciais salvas"
        elif posic == 1:
            cursor1.execute ("CREATE TABLE IF NOT EXISTS credenciais (nome text, email text, senha text, posição text)")
            cursor1.execute("INSERT INTO credenciais VALUES ('"+nome+"','"+email+"','"+senha1+"','consumidor','50')")
            database1.commit()
            statusLabel["text"] = "credenciais salvas"


    def to1():
        escolha.set(1)

    def to0():
        escolha.set(0)

    nameLabel = Label(rootB,text = "digite primeiro e último nome:")
    nameLabel.place(relx=0.01, rely=0.1)

    nameEntry = Entry(rootB)
    nameEntry.place(relx=0.5, rely=0.1)
    

    emailLabel = Label(rootB,text = "digite seu endereço de email:")
    emailLabel.place(relx=0.01, rely=0.25)

    emailEntry = Entry(rootB)
    emailEntry.place(relx=0.5, rely=0.25)

    password1Label = Label(rootB,text = "digite uma senha:")
    password1Label.place(relx=0.01, rely=0.40)

    password1Entry = Entry(rootB,show = "*")
    password1Entry.place(relx=0.5, rely=0.40)

    password2Label = Label(rootB,text = "digite a senha novamente:")
    password2Label.place(relx=0.01, rely=0.55)

    password2Entry = Entry(rootB,show = "*")
    password2Entry.place(relx=0.5, rely=0.55)

    rbLabel = Label(rootB,text = "entrar como:")
    rbLabel.place(relx=0.01, rely=0.7)


    consumerRB = Radiobutton(rootB,text = "consumidor",variable = escolha,value = 1,command = to1)
    consumerRB.place(relx=0.3, rely=0.7)


    ownerRB = Radiobutton(rootB,text = "empregado",variable = escolha, value = 0, command = to0)
    ownerRB.place(relx=0.6, rely=0.7)

    signinButton = Button(rootB,text = "sign-in",command = assinar)
    signinButton.place(relx=0.4, rely=0.85)


    statusLabel = Label(rootB,text = "")
    statusLabel.place(relx=0.6, rely=0.85)

    backButton = Button(rootB,text = "voltar", command = inicio)
    backButton.place(relx = 0,rely = 0)

    rootB.mainloop()

def inicio():
    rootA = Tk()
    rootA.geometry("200x200")
    rootA.title = ("Entrada")
    win = Frame(rootA)
    win.pack()


    welcome = Label(win,text = "Bem vindo ao mercado")
    welcome.pack()

    frame1 = Frame(win,relief = "sunken")
    frame1.pack(padx = 3 , pady = 3, side = TOP)

    frame2 = Frame(win,relief = "sunken")
    frame2.pack(padx = 4 , pady = 4, side = TOP)

    frame3 = Frame(win,relief = "sunken")
    frame3.pack(padx = 5 , pady = 5, side = TOP)

    signin = Button(frame1,text = "sign-in",command = opensignin, width = 15)
    signin.pack(fill = "x")

    tobank = Button(frame2,text = "ATM", command = banco,width = 15)
    tobank.pack(fill = "x")

    tomarket = Button(frame3,text = "para o mercado", command = mercadologin,width = 15)
    tomarket.pack(fill = "x")

    rootA.mainloop()

inicio()