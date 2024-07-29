import networkx as nx
import matplotlib.pyplot as plt
import os #importa lib para limpar tela

def criaGrafo():
  """
    Sumário: Cria grafo a partir das informações de vertices e vizinhos de cada 
    vértice infomadas pelo usuário

    Params: N/D
    
    Retorno:  Print de grafo e propriedades.
  """

  while True:
    try: # Se digitado um int sai do loop
      print("-------------------- Verificar Grafo --------------------\n")
      qtde_vertices = int(input("Informe quantos vertices você deseja usar: "))
      break
    except: # Se não continua no loop
      print("\nOps! Não entendi o que você quis dizer, por favor tente novamente\n")

  contador = 0
  # Inserção do nome dos vertices: enquanto o contador for menor que a 
  # quantidade de vertices ele irá pedir o nome de cada vertice 
  while contador < qtde_vertices:
    while True:
      nome_vertice = input(f"Informe o nome do {contador+1}° vertice: ")
      # se nome do vertice for vazio ou um espaço ele vai mostrar uma mensagem
      # de erro e pedir para o usuário inserir o nome novamente
      if nome_vertice == '' or nome_vertice == ' ': print("\nOps! Não foi informado o nome dos vértices, por favor tente novamente\n")
      else: 
        Grafo.add_node(nome_vertice)
        break
    contador += 1

  os.system("clear")
  print(f"Lista de Vertices: {Grafo.nodes()}")
  print("\nAperte 'Enter' para continuar ")
  confirmacaoUsuario = input('').split(" ")[0]

  # Inserção dos vizinhos de cada vértice
  for vertice in Grafo.nodes():
    os.system("clear")
    while True:
      while True:
        try:
          vizinhos_vertice = int(input(f"\nInforme quantos vizinhos o vertice '{vertice.upper()}' possui: "))
          break
        except: print("\nOps! Não entendi o que você quis dizer, por favor tente novamente\n")

      if vizinhos_vertice < qtde_vertices:
        contador = 0
        while contador < vizinhos_vertice:
          while True:
            aresta_escolhida = input(f"Informe quem é o {contador+1}° vizinho: ")
            
            contador2 = 0
            for vertices in Grafo.nodes():
              if vertices == aresta_escolhida:
                contador2 = 1

            if aresta_escolhida == vertice: print("\nOps! O vizinho informado é o mesmo que o vértice, por favor tente novamente\n")
            elif aresta_escolhida == '': print("\nOps! Não foi informado um vizinho, por favor tente novamente\n")
            elif contador2 != 1: print("\nOps! O vizinho informado não é um vértice, por favor tente novamente\n")
            else: 
              Grafo.add_edge(vertice, aresta_escolhida)
              
              while True:
                try: # Se digitado um int sai do loop
                  peso = int(input(f"Informe o peso para as arestas {vertice} <--> {aresta_escolhida}: "))
                  if peso == '' or peso == ' ': print("\nOps! Não foi informado um peso para as arestas, por favor tente novamente\n")
                  else: 
                    Grafo[vertice][aresta_escolhida]['peso'] = peso
                    break

                except: # Se não continua no loop
                  print("\nOps! Não entendi o que você quis dizer, por favor tente novamente\n")
              break
          contador += 1
        break

      else:
        print('\nOps! O número de vizinhos é maior que a quantidade de vértices possíveis, por favor tente novamente\n')


  plt.figure(1)
  #há vários layouts, mas spring é um dos mais bonitos
  pesos = nx.get_edge_attributes(Grafo,'peso')
  pos =nx.spring_layout(Grafo)
  nx.draw_networkx(Grafo, pos,node_color='green', node_size=400)
  nx.draw_networkx_edges(Grafo,pos,edge_color='blue')
  nx.draw_networkx_edge_labels(Grafo,pos,edge_labels=pesos)

  plt.show()

  print("\n\n--------------------- Propriedades do Grafo acima ---------------------\n")
  # Grafo Completo
  print(f"O grafo {verifica_completo(Grafo)}")
  # Grafo Euleriano
  print(f"O grafo {verifica_euleriano(Grafo.edges(),Grafo.nodes())}")
  # Grafo Nulo
  print(f"O grafo {verifica_nulo(Grafo)}")
  # Grafo Grau Máximo
  print(f"Grau Máximo: {verifica_grau_maximo(Grafo.edges(),Grafo.nodes())}")
  # Grafo Grau Mínimo
  print(f"Grau Mínimo: {verifica_grau_minimo(Grafo.edges(),Grafo.nodes())}")      

def verifica_euleriano(arestas, vertices):
  """
    Sumário: Verificação de grafo para saber se ele é Euleriano.

    Params: Variáveis de arestas e vertices
    
    Retorno: Se o grafo é euleriano ou não
  """
  
  lista = []
  cont_eule = 0
  for k in arestas:
    u = k[0]
    v = k[1]
    lista.append(u)
    lista.append(v)
    
  graus = []
  for num in vertices:
    lista2 = [num,lista.count(num)]
    graus.append(lista2)
  i = 0
  graus2 = graus.copy()
  
  for asdasasd in graus2:
    if i == 0:
      y = asdasasd[1]
      z = asdasasd[0]
    if asdasasd[1]%2 == 0:cont_eule +=1
  i += 1

  if cont_eule == len(vertices): return "é euleriano"
  else: return "não é euleriano"

def verifica_nulo(Grafo):
  """
    Sumário: Verificação de grafo para saber se ele é nulo.

    Params: Var Grafo
    
    Retorno:  Nulo ou não nulo
  """

  if Grafo.edges() == '': return "é nulo"
  else: return "não é nulo"
  
def verifica_completo(Grafo):
  """
    Sumário: Verificação de grafo, quando completo

    Params: Grafo, identico ao verifica_nulo
    
    Retorno:  Completo = True/False
  """

  cont2 = 0
  resultado = "não é completo"

  for vertice in Grafo.nodes():
    cont1 = 0
    for aresta in Grafo.edges(): 
      if (aresta[0] == vertice or aresta[1] == vertice): # se o vertice aparecer em alguma aresta soma mais 1 
        cont1 +=1
        if cont1 == (len(Grafo.nodes())-1): # se a soma de todas as aparições do vertice em alguma aresta for igual ao número de (vertices-1) entao soma mais 1 
          cont2 += 1
          if cont2 == (len(Grafo.nodes())): 
            resultado = "é completo"
  
  return resultado

def verifica_grau_maximo(arestas, vertices):
  """
    Sumário: método para verificação do grau máximo do vértice

    Params: Pega o node da função grafo(a) e o Edge da função Grafo(b)
    
    Retorno: Retorna um print do Grau Máximo
  """

  lista = []
  for k in arestas:
    u = k[0]
    v = k[1]
    lista.append(u)
    lista.append(v)
    
  graus = []
  for num in vertices:
    lista2 = [num,lista.count(num)]
    graus.append(lista2)
  i = 0
  for cont2 in graus:
    if i == 0:
      y = cont2[1]
      z = cont2[0]
    if cont2[1] > y:
      y = cont2[1]
      z = cont2[0]
    i += 1
  return y 

def verifica_grau_minimo(arestas, vertices):
  """
    Sumário: método para verificação do grau máximo do vértice

    Params: Pega o node da função grafo(a) e o Edge da função Grafo(b)
    
    Retorno:  Retorna um print do Grau Mínimo
  """

  lista = []
  for k in arestas:
    u = k[0]
    v = k[1]
    lista.append(u)
    lista.append(v)
    
  graus = []
  for num in vertices:
    lista2 = [num,lista.count(num)]
    graus.append(lista2)

  i = 0
  for cont2 in graus:
    if i == 0:
      y = cont2[1]
      z = cont2[0]
    if cont2[1] < y:
      y = cont2[1]
      z = cont2[0]
    i += 1
  return y 


# Grafos de Exemplo 
def exemplo_grafo_euleriano():
  """
    Sumário: Método para exibição de um grafo euleriano

    Params: N/D
    
    Retorno:  Exemplo de grafo Euleriano
  """

  G5 = nx.Graph()
  G5.add_node('A')
  G5.add_node('B')
  G5.add_node('C')
  G5.add_node('D')
  G5.add_node('E')
  G5.add_node('F')
  G5.add_node('G')

  G5.add_edge('A', 'B')
  G5.add_edge('A', 'D')
  G5.add_edge('B', 'A')
  G5.add_edge('B', 'C')
  G5.add_edge('B', 'E')
  G5.add_edge('B', 'D')
  G5.add_edge('C', 'B')
  G5.add_edge('C', 'E')
  G5.add_edge('D', 'A')
  G5.add_edge('D', 'F')
  G5.add_edge('D', 'E')
  G5.add_edge('E', 'C')
  G5.add_edge('E', 'D')
  G5.add_edge('E', 'G')
  G5.add_edge('E', 'B')
  G5.add_edge('F', 'D')
  G5.add_edge('F', 'G')
  G5.add_edge('G', 'F')
  G5.add_edge('G', 'E')

  nx.draw_networkx(G5, pos=nx.spring_layout(G5), with_labels=True)
  plt.show()

def exemplo_grafo_desconexo():
  """
    Sumário: Print de um exemplo de grafo desconexo, demonstração

    Params: N/D
    
    Retorno:  Demostração de um grafo desconexo
  """

  G4 = nx.Graph()
  G4.add_node('A')
  G4.add_node('B')
  G4.add_node('C')
  G4.add_node('D')
  G4.add_node('E')
  G4.add_node('F')

  G4.add_edge('C', 'A')
  G4.add_edge('B', 'D')
  G4.add_edge('B', 'F')
  G4.add_edge('D', 'B')
  G4.add_edge('D', 'E')
  G4.add_edge('E', 'D')
  G4.add_edge('E', 'F')
  G4.add_edge('F', 'B')
  G4.add_edge('F', 'E')

  #há vários layouts, mas spring é um dos mais bonitos
  nx.draw_networkx(G4, pos=nx.spring_layout(G4), with_labels=True)
  plt.show()

def exemplo_grafo_k4():
  """
    Sumário: Print de um exemplo de grafo K4 (Completo), demonstração

    Params: N/D
    
    Retorno:  Demostração de um grafo Completo
  """

  G3 = nx.Graph()
  G3.add_node('A')
  G3.add_node('B')
  G3.add_node('C')
  G3.add_node('D')

  G3.add_edge('A', 'C')
  G3.add_edge('A', 'B')
  G3.add_edge('A', 'D')
  G3.add_edge('B', 'D')
  G3.add_edge('B', 'A')
  G3.add_edge('B', 'C')
  G3.add_edge('C', 'A')
  G3.add_edge('C', 'B')
  G3.add_edge('C', 'D')

  #há vários layouts, mas spring é um dos mais bonitos
  nx.draw_networkx(G3, pos=nx.spring_layout(G3), with_labels=True)
  plt.show()

def exemplo_grafo_valorado():
  """
    Sumário: Print de um exemplo de grafo valorado, contendo peso, demonstração

    Params: N/D
    
    Retorno:  Demostração de um grafo contendo peso 
  """

  G2 = nx.Graph()
  G2.add_node('A')
  G2.add_node('B')
  G2.add_node('C')
  G2.add_node('D')

  G2.add_edge('A', 'C')
  G2.add_edge('A', 'B')
  G2.add_edge('A', 'D')
  G2.add_edge('B', 'D')
  G2.add_edge('B', 'A')

  G2['A']['C']['peso'] = 5
  G2['A']['B']['peso'] = 10
  G2['A']['D']['peso'] = 2
  G2['B']['D']['peso'] = 4
  G2['B']['A']['peso'] = 8  
  
  pesos = nx.get_edge_attributes(G2,'peso')
  pos =nx.spring_layout(G2)
  nx.draw_networkx(G2, pos,node_color='green', node_size=400)
  nx.draw_networkx_edges(G2,pos,edge_color='blue')
  nx.draw_networkx_edge_labels(G2,pos,edge_labels=pesos)

  plt.show()

def exemplo_grafo_aciclico():
  """
    Sumário: Print de um exemplo de grafo acíclico, contendo peso, demonstração

    Params: N/D
    
    Retorno:  Demostração de um grafo acíclico
  """

  G1 = nx.Graph()
  G1.add_node('v1')
  G1.add_node('v2')
  G1.add_node('v3')
  G1.add_node('v4')

  G1.add_edge('v1', 'v2')
  G1.add_edge('v2', 'v3')
  G1.add_edge('v3', 'v4')

  plt.figure(1)
  #há vários layouts, mas spring é um dos mais bonitos
  nx.draw_networkx(G1, pos=nx.spring_layout(G1), with_labels=True)
  plt.show()

def exemplo_grafo_conexo():
  """
     Sumário: Print de um exemplo de grafo conexo, demonstração

    Params: N/D
    
    Retorno:  Demostração de um grafo conexo
  """

  G = nx.Graph()
  G.add_node('v1')
  G.add_node('v2')
  G.add_node('v3')
  G.add_node('v4')

  G.add_edge('v1', 'v2')
  G.add_edge('v2', 'v3')
  G.add_edge('v3', 'v4')
  G.add_edge('v4', 'v1')

  plt.figure(1)
  #há vários layouts, mas spring é um dos mais bonitos
  nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
  plt.show()

  




Grafo = nx.Graph()
menu = -1
#menu inicial

while menu != 0:
  os.system("clear")

  # Try exception para trativa de erro caso o usuário digite algo dif de número
  while True:
    try:
      print("--------------------  Menu Inicial --------------------")
      menu = int(input("\n0 - Sair\n1 - Verificar grafo\n2 - Exemplos das propriedades\n3 - Sobre\n\n Digite sua opção: "))
      break
    except: print("Ops! Não entendi o que você quis dizer, por favor tente novamente\n")

  
  # opção Sair
  # Se o usuário não deseja sair da aplicação, volta ao loop no menu principal, 
  # se ele deseja, não faz nada saindo assim dos loops
  if menu == 0:
    sair = "" 
    while (sair != "s" and sair != "n"): 
      sair = input("\nTem certeza que deseja sair? (s - sim e n - não): ")

      if sair == "n": menu = -1 
      elif sair != "s": print("\nOps! Não entendi o que você quis dizer, por favor tente novamente") 

  # opção Definir Variáveis
  # Chama a função define_variáveis 
  elif menu == 1: 
    criaGrafo()
    print("\nAperte 'Enter' para continuar ")
    confirmacaoUsuario = input('').split(" ")[0]

  # Opção Exemplos de Propriedades 
  elif menu == 2:
    menu2 = -1
    # Opções para mostrar exemplos de grafos
    while menu2 != 0:
      os.system("clear")
      while True:
        try:
          print("--------------------  Exemplos das Propriedades --------------------\n")
          menu2 = int(input("\n0 - Voltar ao menu inicial\n1 - Grafo Aciclico\n2 - Grafo Conexo\n3 - Grafo Desconexo\n4 - Grafo Valorado\n5 - Grafo Completo(K4)\n6 - Grafo Euleriano\n\n Digite sua opção: "))
          break
        except: print("Ops! Não entendi o que você quis dizer, por favor tente novamente\n")

      if menu2 == 0: menu = -1
      elif menu2 == 1:
        os.system("clear")
        print("\n--------------------- Grafo Aciclico ---------------------\n")
        exemplo_grafo_aciclico()
        print("\nAperte 'Enter' para continuar ")
        confirmacaoUsuario = input('').split(" ")[0]

      elif menu2 == 2:
        os.system("clear")
        print("\n--------------------- Grafo Conexo ---------------------\n")
        exemplo_grafo_conexo()
        print("\nAperte 'Enter' para continuar ")
        confirmacaoUsuario = input('').split(" ")[0]

      elif menu2 == 3:
        os.system("clear")
        print("\n--------------------- Grafo Desconexo ---------------------\n")
        exemplo_grafo_desconexo()
        print("\nAperte 'Enter' para continuar ")
        confirmacaoUsuario = input('').split(" ")[0]

      elif menu2 == 4:
        os.system("clear")
        print("\n--------------------- Grafo Valorado ---------------------\n")
        exemplo_grafo_valorado()
        print("\nAperte 'Enter' para continuar ")
        confirmacaoUsuario = input('').split(" ")[0]

      elif menu2 == 5:
        os.system("clear")
        print("\n--------------------- Grafo Completo(k4) ---------------------\n")
        exemplo_grafo_k4()
        print("\nAperte 'Enter' para continuar ")
        confirmacaoUsuario = input('').split(" ")[0]

      elif menu2 == 6:
        os.system("clear")
        print("\n--------------------- Grafo Euleriano ---------------------\n")
        exemplo_grafo_euleriano()
        print("\nAperte 'Enter' para continuar ")
        confirmacaoUsuario = input('').split(" ")[0]
  elif menu == 3:                                                                                 #Menu Sobre
    os.system("cls")
    print("Ambiente necessário para execução:",
    "\nSistema Operacional: Windows x86 ou x64 (Preferencialmente) ou Distribuição Linux;",
    "\nBibliotecas Python instaladas no sistema escolhido (3.11 ou superior);"
    "\nCompiladores Python (Jupyter, Pycharm, Atom, Spyder, PyDev e outros);",
    "\n\nRequisitos de hardware:",
    "\nProcessador: 1 Núcleo ou superior, 2.6GHz ou superior;",
    "\nRam: 256Mb Livres;",
    "\nInternet: banda de 5Mbps (caso de execução online);",
    "\nArmazenamento: 100Mb de espaço em disco;")
    menu3 = -1
    while menu3 != 0:
      menu3 = int(input("\n0 - Voltar\n1 - informações do programa\n"))
      if menu3 == 1:
        os.system("cls")
        help(criaGrafo)                                                                    #DocString, exibe sumário Tabela Verdade
        help(verifica_nulo) 
        help(verifica_completo)
        help(verifica_grau_maximo)
        help(verifica_grau_minimo) 
        help(exemplo_grafo_euleriano) 
        help(exemplo_grafo_desconexo)
        help(exemplo_grafo_k4)
        help(exemplo_grafo_valorado)
        help(exemplo_grafo_aciclico)
        help(exemplo_grafo_conexo)

  # Se o usuário digitar um número diferente das opções
  else:
    print("\nOps! Não entendi o que você quis dizer, por favor tente novamente. Aperte 'Enter' para continuar")
    confirmacaoUsuario = input('').split(" ")[0]
