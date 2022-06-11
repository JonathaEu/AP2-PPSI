import interface
from PySimpleGUI import PySimpleGUI as sg
import os
from pathlib import Path

#Alterar print
print = sg.Print

#Define "ALTERNANCIA" das janelas
janela1,janela2,janela3,janela4,janela5 = interface.Home1(), None,None,None,None
#Loop de eventos
while True:
    window,event,values = sg.read_all_windows()
    #Extrair dados da interface
   # values = janela1,janela2,janela3.Read()
#comando para fechar
    if  event == sg.WIN_CLOSED:
        break 
#Ir para cadastro de cliente
    if  window == janela1 and event == 'CadastroCliente':
        janela2 = interface.Janela_Cliente()
        janela1.hide()
        sg.Popup('Para exclur cliente somente é necessário informar o nome',title='Dica')
#Ir para cadastro de moto 
    if window == janela1 and event == 'Cadastro Moto':
        janela3 = interface.Janela_Moto()
        janela1.hide()
        sg.Popup('Para excluir motocicleta somente é necessário informar o Modelo da motocicleta',title='Dica')
#Ir para consulta vendas
    if window == janela1 and event == 'Consultar Vendas':
        janela4 = interface.Janela_Cvendas()
        janela1.hide()
#Ir para Efetuar Vendas
    if window == janela1 and event == 'Efetuar Vendas':
        janela5 = interface.Janela_Vendas()
        janela1.hide()
#Ação ao pressionar botao voltar
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()
    if window == janela4 and event == 'Voltar':
        janela4.hide()
        janela1.un_hide()
    if window == janela5 and event == 'Voltar':
        janela5.hide()
        janela1.un_hide()

################### Eventos para botoes #####################
#Chama Escrever cliente
    if window == janela2 and event == 'Cadastrar Cliente':
        escrever()
        sg.Popup('Cliente cadastrado com sucesso, para realizar novo cadastro pressione voltar e selecione a opção de cadastro cliente',title='Informação')

#Chama Alterar cliente
    if window == janela2 and event == 'Alterar Cliente':
        alterarCliente()
        sg.Popup('Dado alterado com sucesso para realizar nova alteração pressione voltar e selecione a opção de cadastro cliente',title='Informação')

#Chama excluir Cliente
    if window == janela2 and event == 'Excluir Cliente':
        excluirCliente()
        sg.Popup('Cliente excluído com sucesso para realizar exclusão novamente, pressione voltar e selecione a opção de cadastro cliente ',title='Informação')

#Chama excluir Moto
    if window == janela3 and event == 'Excluir Motocicleta':
        excluirMoto()
        sg.Popup('Moto cadastrada com sucesso para realizar cadastro novamente, pressione voltar e selecione a opção de cadastro motocicleta',title='Informação')
#Chama Escrever  Moto
    if window == janela3 and event == 'Cadastrar Motocicleta':
        escreverMoto()
        sg.Popup('Moto cadastrada com sucesso para realizar cadastro novamente, pressione voltar e selecione a opçao de cadastro mototicleta',title='Informação')
#Chama Alterar Moto
    if window == janela3 and event == 'Alterar Motocicleta':
        alterarMoto()
        sg.Popup('Moto excluída com sucesso para realizar exclusão novamente, pressione voltar e selecione a opçao de cadastro mototicleta ',title='Informação')
#Chama Realizar VENDA
    if window == janela5 and event == 'Finalizar Venda':
        realizarVenda()
        sg.Popup('Venda realizada com sucesso para realizar outra Venda, pressione voltar e selecione a opção Efetuar Vendas ',title='Informação')

#Função para botão consultar vendas

    if window == janela4 and event == 'Consultar Venda':
         nomeConsulta = values['ModeloVenda']
         #Path = ('vendas/{}'.format(nomeConsulta))
         if os.path.exists('vendas/{}.txt'.format(nomeConsulta)):
             with open('vendas/{}.txt'.format(nomeConsulta),'r') as f:
                consulta = f.readlines()
                print(consulta)
                

    #Funcao Escrever arquivo
    def escrever():
      #  while True:
        if not os.path.exists('CrudCliente'):
            os.mkdir('CrudCliente')
        nomeCliente = values['Nome']
        Path('CrudCliente/{}.txt'.format(nomeCliente)).touch()
        cpf = values['CPF']
        contato = values['Contato']
                    
        listaCliente = ['Nome do Cliente: ' + nomeCliente,'CPF: ' + cpf, 'Contato: ' + contato ]

                    #res = (input("Deseja iniciar um novo cadastro ou sair? Digite 1 e pressione ENTER para continuar, digite 2 e pressione ENTER para sair\n"))    
                    #if res == "2":
                    #   break 
        with open('CrudCliente/{}.txt'.format(nomeCliente),'a') as f:
            f.write(str(listaCliente))         
  
    #Funcao alterar arquivo
    def alterarCliente():
      #  while True:
        if not os.path.exists('CrudCliente'):
            os.mkdir('CrudCliente')
        nomeCliente = values['Nome']
        Path('CrudCliente/{}.txt'.format(nomeCliente)).touch()
        cpf = values['CPF']
        contato = values['Contato']
                    
        listaCliente = ['Nome do Cliente: ' + nomeCliente,'CPF: ' + cpf, 'Contato: ' + contato ]

                    #res = (input("Deseja iniciar um novo cadastro ou sair? Digite 1 e pressione ENTER para continuar, digite 2 e pressione ENTER para sair\n"))    
                    #if res == "2":
                    #   break 
        with open('CrudCliente/{}.txt'.format(nomeCliente),'w') as f:
            f.write(str(listaCliente))         

    #Funcao para EXCLUIR CLIENTE
    def excluirCliente():
        nomeCliente = values['Nome']
        fP = Path('CrudCliente/{}.txt'.format(nomeCliente))
        fP.unlink()
    #Funcao para EXCLUIR Moto
    def excluirMoto():
        nomeMoto = values['Modelo']
        fP = Path('CrudMotocicleta/{}.txt'.format(nomeMoto))
        fP.unlink()
    
    #Funcao escrever arquivos moto
    
    def escreverMoto():
        if not os.path.exists('CrudMotocicleta'):
            os.mkdir('CrudMotocicleta')
        nomeMoto = values['Modelo']
        Path('CrudMotocicleta/{}.txt'.format(nomeMoto)).touch()
        anoF = values['AnoF']
        concess = values['Concess']
        
        listaMoto = ["Nome do modelo:" + nomeMoto, "Concessionária:" + concess, "Ano de fabricação:" + anoF]

        with open('CrudMotocicleta/{}.txt'.format(nomeMoto),'a') as f:
            f.write(str(listaMoto))
    
    #Função pra alterar MOTO
    def alterarMoto():
        if not os.path.exists('CrudMotocicleta'):
            os.mkdir('CrudMotocicleta')
        nomeMoto = values['Modelo']
        Path('CrudMotocicleta/{}.txt'.format(nomeMoto)).touch()
        anoF = values['AnoF']
        concess = values['Concess']
        
        listaMoto = ["Nome do modelo:" + nomeMoto, "Concessionária:" + concess, "Ano de fabricação:" + anoF]

        with open('CrudMotocicleta/{}.txt'.format(nomeMoto),'w') as f:
            f.write(str(listaMoto))
    
    #Funcao para Realizar venda
    def realizarVenda():
        if not os.path.exists('vendas'):
            os.mkdir('vendas')

        nomeVenda = values['ModeloVendido']
        Path('vendas/{}.txt'.format(nomeVenda)).touch()
        nomeCliente = values['NomeComprador']
        
        listaVenda = ['Nome do Comprador:' + nomeCliente, 'Modelo vendido: ' + nomeVenda]
        
        with open('vendas/{}.txt'.format(nomeVenda),'a') as f:
            f.write(str(listaVenda))