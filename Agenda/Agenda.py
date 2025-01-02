agenda = {
    "gustavo": {
        "tel": "999999",
        "email": "gg@gg",
        "endereco": "ggdwshh.huisdf"
    },
    "maria": {
        "tel": "98751",
        "email": "gg@teste@teste.com.br",
        "endereco": "ggdwshh.huisdf"
    },
    "joao": {
        "tel": "912345",
        "email": "joao@teste.com",
        "endereco": "rua abc, 123"
    },
    "ana": {
        "tel": "934567",
        "email": "ana@teste.com",
        "endereco": "av xyz, 456"
    },
    "carlos": {
        "tel": "956789",
        "email": "carlos@teste.com",
        "endereco": "travessa lm, 789"
    },
    "fernanda": {
        "tel": "978123",
        "email": "fernanda@teste.com",
        "endereco": "rua beta, 321"
    },
    "julia": {
        "tel": "982345",
        "email": "julia@teste.com",
        "endereco": "av delta, 654"
    },
    "lucas": {
        "tel": "993567",
        "email": "lucas@teste.com",
        "endereco": "travessa gamma, 987"
    },
    "mariana": {
        "tel": "911223",
        "email": "mariana@teste.com",
        "endereco": "rua omega, 111"
    },
    "pedro": {
        "tel": "922334",
        "email": "pedro@teste.com",
        "endereco": "av theta, 222"
    },
    "beatriz": {
        "tel": "933445",
        "email": "beatriz@teste.com",
        "endereco": "rua sigma, 333"
    },
    "roberto": {
        "tel": "944556",
        "email": "roberto@teste.com",
        "endereco": "travessa tau, 444"
    },
    "lara": {
        "tel": "955667",
        "email": "lara@teste.com",
        "endereco": "av alpha, 555"
    },
    "eduardo": {
        "tel": "966778",
        "email": "eduardo@teste.com",
        "endereco": "rua beta, 666"
    },
    "sophia": {
        "tel": "977889",
        "email": "sophia@teste.com",
        "endereco": "travessa delta, 777"
    },
    "bruno": {
        "tel": "988990",
        "email": "bruno@teste.com",
        "endereco": "av gamma, 888"
    },
    "leticia": {
        "tel": "999101",
        "email": "leticia@teste.com",
        "endereco": "rua epsilon, 999"
    },
    "rafael": {
        "tel": "911212",
        "email": "rafael@teste.com",
        "endereco": "travessa zeta, 121"
    },
    "carolina": {
        "tel": "922323",
        "email": "carolina@teste.com",
        "endereco": "av eta, 232"
    },
    "gabriel": {
        "tel": "933434",
        "email": "gabriel@teste.com",
        "endereco": "rua iota, 343"
    },
    "patricia": {
        "tel": "944545",
        "email": "patricia@teste.com",
        "endereco": "travessa kappa, 454"
    },
    "tiago": {
        "tel": "955656",
        "email": "tiago@teste.com",
        "endereco": "av lambda, 565"
    }
}


def mostrar_contato():
    if agenda:
        for contato in agenda:
            buscar_contato(contato)
            print("------------------")
    else:
        print(">>>> Agenda vazia <<<<")
        
        
def buscar_contato(contato):
    try:
        print("Nome:", contato)
        print("Telefone:", agenda[contato]["tel"])
        print("Email:", agenda[contato]["email"])
        print("Endereco:", agenda[contato]["endereco"])
        print("------------------")
    except KeyError:
        print("Contato inexistente")
    except:
        print("Algum erro inesperado")
   
   
def ler_detalhes():
    tel = input("Digite o número de telefone: ")
    email = input("Digite o email: ")
    endereco = input("Digite o endereço: ")
    return tel,email,endereco 
        

def incluir_editar_contato(contato,tel,email,endereco):
    try:
        agenda[contato]= {
            "tel": tel,
            "email": email,
            "endereco": endereco
        }
        save()
        print(">>>>>>> O contato {} foi adicionado/editado com sucesso <<<<<<<<".format(contato))
    except KeyError:
        print("Contato inexistente")
    except:
        print("Algum erro inesperado")

def excluir_contato(contato):
    try:
        agenda.pop(contato)
        save()
        print(">>>> O contato {} foi deletado com sucesso <<<<".format(contato))
    except KeyError:
        print("Contato inexistente")
    except:
        print("Algum erro inesperado")
        
        
def save():
    exportar_arquivo("database.csv")
    
    
def carregar():
    try:
        with open("database.csv", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(",")
                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                
                agenda[nome]= {
                    "tel": tel,
                    "email": email,
                    "endereco": endereco
                }
        print(">>>>>>> Database carregado com sucesso <<<<<<<")
        print(">>> {} contados carregados <<<<".format(len(agenda)))
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as e:
        print("Ocorreu um erro")
        print(e)
    
    
    
def exportar_arquivo(filename):
    try:
        with open(filename, "w") as arquivo:
            arquivo.write("nome,telefone,email,endereco\n")
            for contato in agenda:
                tel = agenda[contato]["tel"]
                email = agenda[contato]["email"]
                endereco = agenda[contato]["endereco"]
                arquivo.write("{},{},{},{}\n".format(contato,tel,email,endereco))
        print(">>>> Agenda exportada com sucesso <<<<")
    except Exception as e:
        print("Algum erro ocorreu")
        print(e)
        
        
def importar_contato(filename):
    try:
        with open(filename, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(",")
                nome = detalhes[0]
                tel = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                
                incluir_editar_contato(nome,tel,email,endereco)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as e:
        print("Ocorreu um erro")
        print(e)


def imprimir_menu():
    print("1 - Mostrar todos os contatos da agenda")
    print("2 - Buscar contato da agenda")
    print("3 - Adicionar novo contato")
    print("4 - Editar contato")
    print("5 - Remover contato da agenda")
    print("6 - Exportar contatos")
    print("7 - Importar contatos")
    print("0 - Fechar menu")
    
  
carregar()    
while True:
    imprimir_menu()
    opcao = (input("Escolha uma das opções acima e digite: "))
    if opcao == "1":
        mostrar_contato()
    elif opcao == "2":
        contato = input("Digite o contato que você deseja buscar: ")
        buscar_contato(contato)
    elif opcao == "3":
        contato = input("Digite o contato: ")
        try:
            agenda[contato]
            print(">>> Contato já existe <<<")
        except KeyError:
            tel,email,endereco = ler_detalhes()
            incluir_editar_contato(contato,tel,email,endereco)
    elif opcao == "4":
        contato = input("Digite o contato: ")
        try:
            agenda[contato]
            print(">>> Editando contato <<<", contato)
            tel,email,endereco = ler_detalhes()
            incluir_editar_contato(contato,tel,email,endereco)
        except KeyError:
            print(">>>>>> Contato inexistente<<<<<<")
    elif opcao == "5":
        contato = input("Digite o contato que você deseja remover: ")
        excluir_contato(contato)
    elif opcao == "6":
        filename = input("Digite o nome do arquivo a ser exportado")
        exportar_arquivo(filename)
    elif opcao == "7":
        filename = input("Digite o nome do arquivo: ")
        importar_contato(filename)
    elif opcao == "0":
        print("Fechando a agenda...")
        break
    else:
        print("Opção inválida")