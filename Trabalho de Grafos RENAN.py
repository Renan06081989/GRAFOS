def dfs(graph, node, y):
    if node == y : print("Você chegou a seu destino!")
    if node == 'Monteiro' or node == 'Sumé' or node == 'Santa Luzia do Cariri' or node == 'Serra Branca' or node == 'São João do Cariri' or node == 'Malhada da Roça' or node == 'Boa Vista' or node == 'Campina Grande' or node == 'João Pessoa':
        print(node)
    if node != 'Monteiro' and node != 'Sumé' and node != 'Santa Luzia do Cariri' and node != 'Serra Branca' and node != 'São João do Cariri' and node != 'Malhada da Roça' and node != 'Boa Vista' and node != 'Campina Grande' and node != 'João Pessoa':
        n = float(node)
        if n == 34.0 or n == 12.0 or n == 21.0 or n == 18.0 or n == 19.0 or n == 46 or n == 107.0 :
            m = int(n)
            print(m,'min')
            cba.append(m)
        else:
            print(n,'Km')
            abc.append(n)
    if node != y :
        for neighbour in graph[node]:
            dfs(graph, neighbour, y)


#Loop do Menu
z = 0 
while z == 0:        
    abc = []
    cba = []

    #Menu
    print("             MIRAGEM BUSS")
    print()
    print("Escolha uma rota!" )
    print()
    print("digite (1) para (Monteiro --> João Pessoa)")
    print("digite (0) para (João Pessoa --> Monteiro)")
    a = input()
    if (a != "1") and (a != "0" ):
        print("Querido usuário, digite o número correspondente a rota desejada!")
        a = str(input())
    if (a != "1") and (a != "0" ):
        print("Você está me desafiando??")
        a = str(input())
    while (a != "1") and (a != "0" ):
            print("fique a vontade, estou em loop!")
            a = str(input())    
    print()


    #(Monteiro --> João Pessoa)               
    if (a == "1"):
        graph={
            'Monteiro':['37.1','34','Sumé'],
            '37.1':[],
            '34':[],
            'Sumé':['11','12','Santa Luzia do Cariri'],
            '11':[],
            '12':[],
            'Santa Luzia do Cariri':['22.2','21','Serra Branca'],
            '22.2':[],
            '21':[],
            'Serra Branca':['19.7','18','São João do Cariri'],
            '19.7':[],
            '18':[],
            'São João do Cariri':['20.8','18','Malhada da Roça'],
            '20.8':[],
            'Malhada da Roça':['21.8','19','Boa Vista'],
            '21.8':[],
            '19':[],
            'Boa Vista':['44.1','46','Campina Grande'],
            '44.1':[],
            '46':[],
            'Campina Grande':['126.5','107','João Pessoa'],
            '126.5':[],
            '107':[],
            'João Pessoa':[]
        }
        print("  Rota Miragem Buss (Monteiro - João pessoa)")
        print()
        g = 0
        while g == 0:
            x = input("Digite a cidade que deseja partir: ").title() # Transforma a entrada em título
            y = input("Digite a cidade que deseja chegar: ").title() # Transforma a entrada em título
            print()
            if x == 'Monteiro' or x == 'Sumé' or x == 'Santa Luzia do Cariri' or x == 'Serra Branca' or x == 'São João do Cariri' or x == 'Malhada da Roça' or x == 'Boa Vista' or x == 'Campina Grande' or x == 'João Pessoa':
                if y == 'Monteiro' or y == 'Sumé' or y == 'Santa Luzia do Cariri' or y == 'Serra Branca' or y == 'São João do Cariri' or y == 'Malhada da Roça' or y == 'Boa Vista' or y == 'Campina Grande' or y == 'João Pessoa':
                    print("Cidades em que o Ônibus irá percorrer para chegar ao seu destino!")
                    print()
                    print("Apertem os cintos...")
                    print("visitando...")
                    g = 1
                    dfs(graph, x, y)
            

    #(João Pessoa --> Monteiro)        
    elif (a == "0"):
        graph={
            'João Pessoa':['126.5','107','Campina Grande'],
            '126.5':[],
            '107':[],
            'Campina Grande':['44.1','46','Boa Vista'],
            '44.1':[],
            '46':[],
            'Boa Vista':['21.8','19','Malhada da Roça'],
            '21.8':[],
            '19':[],
            'Malhada da Roça':['20.8','18','São João do Cariri'],
            '20.8':[],
            '18':[],
            'São João do Cariri':['19.7','18','Serra Branca'],
            '19.7':[],
            'Serra Branca':['22.2','21','Santa Luzia do Cariri'],
            '22.2':[],
            '21':[],
            'Santa Luzia do Cariri':['11','12','Sumé'],
            '11':[],
            '12':[],
            'Sumé':['37.1','34','Monteiro'],
            '37.1':[],
            '34':[],
            'Monteiro':[]
        }
        print("  Rota Miragem Buss (João pessoa - Monteiro)")
        print()
        g = 0
        while g == 0:
            x = input("Digite a cidade que deseja partir: ").title() # Transforma a entrada em título
            y = input("Digite a cidade que deseja chegar: ").title() # Transforma a entrada em título
            print()
            if x == 'Monteiro' or x == 'Sumé' or x == 'Santa Luzia do Cariri' or x == 'Serra Branca' or x == 'São João do Cariri' or x == 'Malhada da Roça' or x == 'Boa Vista' or x == 'Campina Grande' or x == 'João Pessoa':
                if y == 'Monteiro' or y == 'Sumé' or y == 'Santa Luzia do Cariri' or y == 'Serra Branca' or y == 'São João do Cariri' or y == 'Malhada da Roça' or y == 'Boa Vista' or y == 'Campina Grande' or y == 'João Pessoa':
                    print("Cidades em que o Ônibus irá percorrer para chegar ao seu destino!")
                    print()
                    print("Apertem os cintos...")
                    print("visitando...")
                    g = 1
                    dfs(graph, x, y)


    #Calcular a distância
    dist = 0
    for i in range(len(abc)):
        dist += abc[i]

    #Calcular o tempo
    temp = 0
    for i in range(len(cba)):
        temp += cba[i]
        
        
    print()
    print('A distancia total a ser percorrida na viagem será: {:.1f} Km'.format(dist))
    print()
    if temp >= 60:
        t = temp//60
        m = temp%60
        print('o tempo total da viagem será: {:.0f}h e {:.0f} min'.format(t,m))
    else:
        print('o tempo total da viagem será: {:.0f} min'.format(temp))
        
    print()
    print()
    menu = input('Aperte "enter" para voltar ao Menu! ')
    print()
    print()
    print()
    
