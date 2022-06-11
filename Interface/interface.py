from PySimpleGUI import PySimpleGUI as sg

#Layout 
def Home1():
    sg.theme('Dark Grey 13')
    layout = [
        
        [sg.Button('CadastroCliente',size=(18,0),font=("Times New Roman",45))],
        [sg.Button('Cadastro Moto',size=(18,0),font=("Times New Roman",45))],
        [sg.Button('Consultar Vendas',size=(18,0),font=("Times New Roman",45))],
        [sg.Button('Efetuar Vendas',size=(18,0),font=("Times New Roman",45))],
        [sg.Canvas(size=(400,50))]
    ]
    
    return sg.Window('Sistema Hunter Motors', layout=layout, finalize=True)


def Janela_Cliente():
    sg.theme('Dark Grey 13')
    layout = [
        [sg.Text('Insira os dados cadastrais',font=('Times',40),text_color='#F8F8FF')],
        [sg.Text('Nome    ',text_color='#F8F8FF', font=('Times',16)),sg.Input(size=(48,1),key='Nome')],
        [sg.Text('CPF      ',text_color='#F8F8FF', font=('Times',16)),sg.Input(size=(48,1),key='CPF')],
        [sg.Text('Contato',text_color='#F8F8FF', font=('Times',16)),sg.Input(size=(20,1),key='Contato')],
        [sg.Text('\n')],
        [sg.Button('Cadastrar Cliente',size=(0,0),font=("Times New Roman",15)),
        sg.Button('Alterar Cliente',size=(0,0),font=("Times New Roman",15)),
        sg.Button('Excluir Cliente',size=(0,0),font=("Times New Roman",15)),
        sg.Button('Voltar',size=(0,0),font=("Times New Roman",15))],

        [sg.Canvas(size=(400,20))]
    ]
    
#Janela
    return sg.Window('Controle Cliente', layout=layout, finalize=True)
   
def Janela_Moto():
    sg.theme('Dark Grey 13')
    layout = [
        [sg.Text('Insira os dados cadastrais',font=('Times',35), text_color='#F8F8FF')],
        [sg.Text('Modelo                  ', text_color='#F8F8FF', font=('Times',16)),sg.Input(size=(48,1),key='Modelo')],
        [sg.Text('Ano de Fabricação', text_color='#F8F8FF', font=('Times',16)),sg.Input(size=(48,1),key='AnoF')],
        [sg.Text('Concessionária     ', text_color='#F8F8FF', font=('Times',16)),sg.Input(size=(20,1),key='Concess')],
        [sg.Button('Cadastrar Motocicleta',size=(0,0),font=("Times New Roman",15)),
        sg.Button('Alterar Motocicleta',size=(0,0),font=("Times New Roman",15)),
        sg.Button('Excluir Motocicleta',size=(0,0),font=("Times New Roman",15)),
        sg.Button('Voltar',size=(0,0),font=("Times New Roman",15))],
        
        [sg.Canvas(size=(400,20))]
    ]
    #Janela
    return sg.Window('Controle Moto', layout=layout, finalize=True)

    #janela CONSULTA VENDAS
def Janela_Cvendas():
    layout = [
    [sg.Text('Insira o modelo da moto para consultar a venda',font=('Times',35), text_color='#F8F8FF')],
    [sg.Text('     Modelo   ', text_color='#F8F8FF', font=('Times',16)),sg.Input(size=(48,1),key='ModeloVenda')],
    [sg.T('                                                     ')],
    [sg.T('                                                     ')],
    [sg.T('                                                     '),sg.Button('Consultar Venda',size=(30,0),font=("Times New Roman",15)),
    sg.Button('Voltar',font=("Times New Roman",15))],
    [sg.Canvas(size=(400,50))]
    ]
    return sg.Window('Consulta de Vendas', layout=layout, finalize=True)

#Janela de efetuar vendas
def Janela_Vendas():
    layout = [
    [sg.Text('Insira os dados cadastrados',font=('Times',35), text_color='#F8F8FF')],
    [sg.Text('Nome do comprador                  ',text_color='#F8F8FF', font=('Times',16)),sg.Input(size=(48,1),key='NomeComprador')],
    [sg.Text('Modelo da motocicleta vendida', text_color='#F8F8FF', font=('Times',16)),sg.Input(size=(48,1),key='ModeloVendido')],
    [sg.Button('Finalizar Venda',pad=(300,80),font=("Times New Roman",15)),
    sg.Button('Voltar',pad=(0,80),font=("Times New Roman",15))],
    [sg.Canvas(size=(400,0))]
    ]
    
    return sg.Window('Vendas', layout=layout, finalize=True)